import pytest
from s3.s3_utils import uploadToS3, downloadFromS3

def testS3UploadDownload():
    # Upload and download a file from S3 to check if it works correctly
    bucket = 'dashboard-test-data'  # If pushing this online, use environment variables instead of hardcoding
    key = 'testNBA_data.json'
    testData = {'message': 'see my message'}

    print(f"Uploading test data to S3 bucket: {bucket}")
    uploadToS3(bucket, key, testData)

    print(f"Downloading test data from S3 bucket: {bucket}")
    retrievedData = downloadFromS3(bucket, key)

    if retrievedData == testData:
        print("Test passed: Uploaded and retrieved data match.")
    else:
        print("Error: Retrieved data does not match uploaded data.")

def testS3InvalidDownload():
    # Try to download a file that doesn't exist and handle the error properly
    bucket = 'dashboard-Ftest-data'
    key = 'non_existent.json'

    print(f"Attempting to download a non-existent file: {key} from {bucket}")

    try:
        data = downloadFromS3(bucket, key)
        print("Error: Expected failure but was able to download data.")
    except Exception as e:
        print(f"Test passed: Could not download non-existent file. Error: {e}")
