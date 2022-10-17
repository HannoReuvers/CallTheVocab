### IMPORT LIBRARIES ###
import json, os, random

### CURRENT DIRECTORY ###
CurrentDirectory = os.path.dirname(__file__)

### IMPORT FUNCTIONS ###
FunctionFileLocation = os.path.join(CurrentDirectory, "functions/AppFunctions.py")
exec(open(FunctionFileLocation).read())

### IMPORT DATA ###
#DataFile = "DieciLezioniItaliano_Ch1.json"
DataFile = "IlPiccoloPrincipe_Ch1.json"
DataFileLocation = os.path.join(CurrentDirectory, "data/"+DataFile)
with open(DataFileLocation, "r") as OpenFile:
    Questions = json.load(OpenFile)

### MAIN ###
QuestionList = list(range(len(Questions)))
random.shuffle(QuestionList)

### INITIALIZE COUNTERS ###
Mistakes = 0; Complete = 0

### START TEST ###
print("\n")
while QuestionList:

    #--- Current question ---#
    q = QuestionList[0]

    #--- Print progress bar ---#
    PrintProgressBar(Complete, len(Questions))

    #--- Ask question ---#
    if Questions[q]["QuestionType"] == "Open":
        CorrectAnswer = AskOpenQuestion(Questions[q])
    elif Questions[q]["QuestionType"] == "VOC":
        CorrectAnswer = AskVocabularyQuestion(Questions[q])
    else:
        print("Error")
    QuestionList.pop(0)

    #--- Keep track of progress ---#
    if CorrectAnswer:
        Complete +=1
    else:
        Mistakes  +=1
        QuestionList.append(q)
    print("\n")

### REPORT RESULT ###
PrintProgressBar(Complete, len(Questions))
print("Number of words practiced: ", len(Questions))
print("Number of errors: ", Mistakes)
