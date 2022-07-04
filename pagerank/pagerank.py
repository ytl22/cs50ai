import os
import random
import re
import sys
import numpy as np

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_distribute = {} # initialize probability distribution dictionary
    total_page = len(corpus) # number of page in corpus
    
    # Calculate probabilty p
    if len(corpus[page]) == 0:
        # if no outgoing links on current page
        # for all pages
        p = 1 / total_page
        for page_name in corpus.keys():
            prob_distribute[page_name] = p
        return prob_distribute
    else:
        # For each outlink page
        p = (1 - damping_factor) / len(corpus) + \
            damping_factor / len(corpus[page])

    for page_name in corpus.keys():
        if page_name in corpus[page]:
            prob_distribute[page_name] = p
        else:
            prob_distribute[page_name] = (1 - damping_factor) / len(corpus)

    
    return prob_distribute

    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Inititalize estimated Pagerank
    pagerank = {}
    for page_name in corpus.keys():
        pagerank[page_name] = 0

    # randomly choose a page
    total_page = len(corpus)
    page = random.choice(list(corpus.keys()))
    pagerank[page] = 1/n
    samples = 1 # number of sample generated

    # generate rest of the sample
    while samples != n:
        # Get probability distribution base on previous sample
        p_dist = transition_model(corpus, page, damping_factor)
        # Choose page base on transition probabilities
        page = random.choices(list(p_dist.keys()), weights = list(p_dist.values()), k = 1)[0]
        # Update probability
        pagerank[page] += 1/n

        # samples number increment
        samples += 1

    return pagerank


    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Inititalize estimated Pagerank
    prev_pagerank = {}
    for page in corpus.keys():
        prev_pagerank[page] = 1 / len(corpus)

    max_changes = 1
    # Until no pagerank value changes by more than 0.001
    while max_changes > 0.001:
        new_pagerank = {}

        # Calculate new pagerank for each page
        for page in prev_pagerank.keys():

            new_pagerank[page] = (1 - damping_factor) / len(corpus)

            # pages that links to page
            
            for page_name, links in corpus.items():
                # pages that links to the page
                if (page_name != page) and (page in links):
                            
                    numlinks = len(corpus[page_name])
                    new_pagerank[page] += damping_factor * (prev_pagerank[page_name]) / numlinks

                # page with no links
                elif len(links) == 0:
                    new_pagerank[page] += damping_factor * (prev_pagerank[page_name]) / len(corpus)


        old_value = np.array(list(prev_pagerank.values()))
        new_value = np.array(list(new_pagerank.values()))

        max_changes = max(abs((new_value - old_value)))

        prev_pagerank = new_pagerank.copy()

    return new_pagerank


    raise NotImplementedError


if __name__ == "__main__":
    main()
