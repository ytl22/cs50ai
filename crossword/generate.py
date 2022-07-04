import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
       
        for var in self.domains:
            new_domains = self.domains[var].copy()
            for word in self.domains[var]:
                if len(word) != var.length:
                    new_domains.remove(word)
                self.domains[var] = new_domains
        

        #raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
       
        if self.crossword.overlaps[x, y] == None:
            return False
        else:
            (i,j) = self.crossword.overlaps[x, y]
            
        revised = False
        new_domain = self.domains[x].copy()

        for word_x in self.domains[x]:
            
            match = False

            for word_y in self.domains[y]:
                try:
                    if word_x[i] == word_y[j]:
                        match = True
                        break
                except:
                    continue

            if not match:
                new_domain.remove(word_x)
                revised = True

        self.domains[x] = new_domain
     

        return revised
        #raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        q = []
        if arcs == None:
            for var in self.crossword.variables:
                for neighbour in self.crossword.neighbors(var):
                    q.append((var, neighbour))
        else:
            q = arcs[:]

        while len(q) != 0:
            (x, y) = q[0]
            q.pop(0)

            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False

                for var in self.crossword.neighbors(x):
                    if var != y:
                        q.append((var, x))

        return True
        
        #raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.domains:
            if var not in assignment:
                return False
        return True
        #raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        words = list(assignment.values())

        if len(words) != len(set(words)):
            return False

        for var in assignment:
            if var.length != len(assignment[var]):
                return False
            for y in self.crossword.neighbors(var):
                (i,j) = self.crossword.overlaps[var, y]
                if y in assignment and assignment[var][i] != assignment[y][j]:
                    return False

        return True
        #raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        domain = []
        for word in self.domains[var]:
            n = 0
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    continue

                i, j = self.crossword.overlaps[var, neighbor]
                for word_neighbor in self.domains[neighbor]:
                    if word[i] != word_neighbor[j]:
                        n += 1
            domain.append((word, n))

        domain.sort(key = lambda word:word[1])

        return [word[0] for word in domain]

        #raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned = [None]
        smallest_domain = None
        for var in self.crossword.variables:
            if var in assignment:
                continue
            if smallest_domain == None:
                unassigned[0] = var
            elif len(self.domains[var]) < smallest_domain:
                unassigned[0] = var
            elif len(self.domains[var]) == smallest_domain:
                unassigned.append(var)

        if len(unassigned) == 1:
            return unassigned[0]
        
        var_degree = []
        for var in unassigned:
            var_degree.append(var, len(self.crossword.neighbors(var)))

        var_degree.sort(key = lambda degree:degree[1])

        return var_degree[0][0]

        raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        

        if self.assignment_complete(assignment):
            return assignment

        unassigned = self.select_unassigned_variable(assignment)
        order_domain = self.order_domain_values(unassigned, assignment)

        for word in order_domain:

            assignment[unassigned] = word
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[unassigned]
            else:
                del assignment[unassigned]

        return None

        raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
