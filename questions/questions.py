import nltk
import sys
import os
import string
import math


FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    content = {}

    for file in os.listdir(directory):
        with open(os.path.join(directory, file), "r", encoding="utf-8") as f:
            content[file] = f.read()

    return content
    #raise NotImplementedError


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    document = document.lower()

    words = nltk.tokenize.word_tokenize(document)

    punctuation = string.punctuation
    stopword = nltk.corpus.stopwords.words("english")

    filtered = [word for word in words if (not word in stopword and not word in punctuation)]

    return filtered
    #raise NotImplementedError


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idf = {}
    document_freq = {}

    for doc in documents.keys():
        words = set(documents[doc])
        for word in words:
            try:
                document_freq[word] += 1
            except:
                document_freq[word] = 1

    NUM_OF_DOC = len(documents)

    for word, count in document_freq.items():
        idf[word] = math.log(NUM_OF_DOC/count)

    return idf

    #raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """


    tf_idf = {file:0  for file in files}

    for word in query:
        try:
            word_idf = idfs[word]
        except:
            continue
        for doc in files:
            count = files[doc].count(word)
            tf_idf[doc] += count * word_idf

    top_n = [key for key, value in sorted(tf_idf.items(), key = lambda item: item[1], reverse = True)]

    return top_n[0:n]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    
    idf = {s:0 for s in sentences}
    density = {s:0 for s in sentences}
    for word in query:
        try:
            word_idf = idfs[word]

        except:
            continue

        for s in sentences:
            if word in sentences[s]:
                idf[s] += word_idf
                density[s] += 1

    for s, v in density.items():
        density[s] = v/len(sentences[s])

    s_idf_d = []
    for s in sentences:
        s_idf_d.append((s, idf[s], density[s]))

    top_n = [s for s, idf, d in sorted(s_idf_d, key = lambda x: (x[1],x[2]), reverse = True)]

    return top_n[0:n]
    #raise NotImplementedError


if __name__ == "__main__":
    main()
