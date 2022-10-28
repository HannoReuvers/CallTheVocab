'''
--------------
    Function to upload vocabulary file to Amazon S3.
--------------
inputs (on command line):
    (1) File to upload
    (2) Amazon S3 bucket name
    (3) Name (or key) of the S3 resource
'''

import boto3, json, os, sys

# Check user input (NOTE: element 0 is the function name)
if len(sys.argv)!=4:
    sys.exit("Please provide exactly three inputs: (1) file to upload, (2) Amazon S3 bucket, (3) name inside S3 bucket")

# Reassign input
FileName = str(sys.argv[1])
BucketName = str(sys.argv[2])
TargetName = str(sys.argv[3])

# JSON file location (searches in current folder!)
CurrentDirectory = os.path.dirname(__file__)
DataFileLocation = os.path.join(CurrentDirectory, FileName)

# Print overview for user
print("\n-----------------")
print("File to upload: ", DataFileLocation)
print("S3 bucket name: ", BucketName)
print("Filename in S3 bucket: ", TargetName)
print("-----------------\n")

# Ask confirmation
UserReply = input("Do you wish to upload vocabulary to DynamoDB? Type \"agree\" to proceed.\n")
if UserReply!="agree":
    sys.exit("Program terminated because user did not agree to continue.")

# Connect to DynamoDB resource and upload file
s3_client = boto3.client("s3")
response = s3_client.upload_file(FileName, BucketName, TargetName)
