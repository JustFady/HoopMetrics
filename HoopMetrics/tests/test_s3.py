import pytest
from s3.s3_utils import uploadToS3, downloadFromS3

def testS3UploadDownload():
    # Upload a small test JSON file to S3 and download it back
    bucket = 'dashboard-test-data'  # When pushing this online, make sure to use environment variables instead
    key = 'testNBA_data.json'
    testData = {'message': 'hello world'}
    uploadToS3(bucket, key, testData)
    retrievedData = downloadFromS3(bucket, key)
    assert retrievedData == testData

def testS3InvalidDownload():
    #testing what happens when trying to fetch a non-existent file
    bucket = 'dashboard-Ftest-data'
    key = 'non_existent.json'
    try:
        downloadFromS3(bucket, key)
        assert False  #if it gets here, test should fail
    except:
        assert True  #expecting failure
