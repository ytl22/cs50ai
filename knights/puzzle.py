from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # If A is Aknight, A tells the truth
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is Aknave, A lies
    Implication(AKnave, Not(And(AKnight, AKnave))),
    # A is either knight or knave
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either knight or knave
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),

    # B is either knight or knave
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),

    # If A is knight
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is knave
    Implication(AKnave, Not(And(AKnave, BKnave))),

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either knight or knave
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),

    # B is either knight or knave
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),

    # If A is knight, both are the same kind
    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),

    # If A is knave, not both are same kind
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),

    # If B is knight, they are different kinds
    Implication(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),

    # If B is knave, they are not different kind
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave)))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either knight or knave
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),

    # B is either knight or knave
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),

    # C is either knight or knave
    Not(And(CKnight, CKnave)),
    Or(CKnight, CKnave), 

    # If A is knight 
    Implication(AKnight, Or(AKnight, AKnave)),
    # If A is knave
    Implication(AKnave, Not(Or(AKnave, AKnight))),

    # If B is knight
    Implication(BKnight, And(
        # A said I am a knave
        Implication(AKnight, AKnave),
        Implication(AKnave, AKnight),
        # C is a knave
        CKnave
        )),  
    # If B is knave
    Implication(BKnave, Not(And(
        # A said I am a knave
        Implication(AKnight, AKnave),
        Implication(AKnave, AKnight),
        # C is a knave
        CKnave
        ))),

    # If C is knight
    Implication(CKnight, AKnight),

    # If C is knave
    Implication(CKnave, Not(AKnight))  
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
