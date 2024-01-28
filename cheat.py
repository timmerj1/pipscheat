"""Defines a cheat function for PIPS python assignments"""

def cheat(question: str = "2.2P.11"):
    """Prints code to solve python questions for PIPS at UvA

    Parameters:
    question (str): question you need help with, include P for Python questions.
    Do not start `question` with Q.
    """
    if question is "2.2P.11":
        with open("videopoker.py", encoding="utf8") as file:
            out = file.readlines()
    elif question in ["2.2P.9", "2.2P.10"]:
        with open("sequences.py", encoding="utf8") as file:
            out = file.readlines()
    else:
        filename = "Assignment_" + question[0:3] + ".py"
        with open(filename, encoding="utf8") as file:
            lines = file.readlines()
        start = lines.index("## Q" + question + "\n")
        next_number = str(int(question.split(".")[-1]) + 1)
        next_question = question.replace(question.split(".")[-1], next_number)
        next_Q = "## Q" + next_question + "\n"
        if next_Q in lines:
            end = lines.index(next_Q)
        else:
            end = -1
        out = lines[start:end]
    for i in out:
        print(i)