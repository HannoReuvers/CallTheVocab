# Functions
def AskOpenQuestion(question):
    print(question["Question"])                 # Print question to screen
    UserAnswer = input("Your answer: ")         # User input
    # Grading
    if UserAnswer==question["Correct"]:
        print("Well done!")
        return True
    else:
        print("Correct answer: ", question["Correct"])
        return False

def AskVocabularyQuestion(question):
    print("Translate to Italian: ", question["EnglishWord"])
    UserAnswer = input("Your answer: ")
    # Grading
    if UserAnswer==question["ItalianWord"]:
        print("Well done!")
        return True
    else:
        print("Correct answer: ", question["ItalianWord"])
        return False

def PrintProgressBar(TasksFinished, TotalTasks):
    i = int(30*TasksFinished/TotalTasks)
    print( "[%-30s] %d%%" % ('='*i, int(100*TasksFinished/TotalTasks)) )
