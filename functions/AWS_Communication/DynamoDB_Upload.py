'''
--------------
    Function to upload vocabulary file to DynamoDB.
--------------
inputs (on command line):
    (1) json vocabulary file
    (2) DynamoDB table name (needs to exist already)
    (3) Book title
    (4) Chapter
Notes:
    - The book title and chapter are combined in a string to generate the partition key.
    - The question number is the sort key.
    - Combination partition key + sort key is unique (as required)
'''

import boto3, json, os, sys

# Check user input (NOTE: element 0 is the function name)
if len(sys.argv)!=5:
    sys.exit("Please provide exactly four inputs: (1) json vocabulary file, (2) DynamoDB table name, (3) book title, and (4) chapter number")

# Reassign input
JSONfile = str(sys.argv[1])
DynamoDBTable = str(sys.argv[2])
BookTitle = str(sys.argv[3])
ChapterNumber = str(sys.argv[4])

# JSON file location (searches in current folder!)
CurrentDirectory = os.path.dirname(__file__)
DataFileLocation = os.path.join(CurrentDirectory, JSONfile)

# Print overview for user
print("\n-----------------")
print("JSON file: ", DataFileLocation)
print("DynamoDB table name: ", DynamoDBTable)
print("Book title: ", BookTitle)
print("Chapter number: ", ChapterNumber)
print("-----------------\n")

# Ask confirmation
UserReply = input("Do you wish to upload vocabulary to DynamoDB? Type \"agree\" to proceed.\n")
if UserReply!="agree":
    sys.exit("Program terminated because user did not agree to continue.")

# Connect to DynamoDB resource
dynamodb = boto3.resource("dynamodb")
CurrentTable = dynamodb.Table("ItalianVocabulary")

# Load questions from JSON file
with open(DataFileLocation, "r") as OpenFile:
    Questions = json.load(OpenFile)

# Write to AWS DynamoDB: use put_item() as number of writes may exceed 25, see:
# [https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html]
QuestionCounter = 0
for q in Questions:

    # Increase question counter
    QuestionCounter += 1

    # Write JSON content to DynamoDB
    if q["QuestionType"]=="Open":
        CurrentTable.put_item(
            Item={
                "Book": BookTitle+"_Ch_"+ChapterNumber,
                "ChapterQuestion": str(QuestionCounter),
                "QuestionType": q["QuestionType"],
                "Question": q["Question"],
                "Correct": q["Correct"],})
    elif q["QuestionType"]=="VOC":
        CurrentTable.put_item(
            Item={
                "Book": BookTitle+"_Ch_"+ChapterNumber,
                "ChapterQuestion": str(QuestionCounter),
                "QuestionType": q["QuestionType"],
                "ItalianWord": q["ItalianWord"],
                "EnglishWord": q["EnglishWord"],})
    else:
        sys.exit("Unknown question type encountered. I stop writing to DynamoDB.")
