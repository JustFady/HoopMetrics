import boto3
from configparser import ConfigParser

# Load my S3 credentials from config file (Make sure this file is NOT uploaded to GitHub)
def loadS3Config(filename='config/s3_config.ini', section='aws'):
    parser = ConfigParser()
    parser.read(filename)
    s3Config = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            s3Config[param[0]] = param[1]

    return s3Config

# Upload a file to my S3 bucket (Make sure AWS credentials are set up correctly)
def uploadFileToS3(localFile, bucketName, s3Key=None):
    creds = loadS3Config()

    # Initialize the S3 client (standard way to do this with Boto3)
    s3 = boto3.client(
        's3',
        aws_access_key_id=creds['aws_access_key_id'],
        aws_secret_access_key=creds['aws_secret_access_key'],
        region_name=creds['region']
    )

    # If no S3 key is provided, just use the filename
    if not s3Key:
        s3Key = localFile

    # Upload file to S3 (this will overwrite if it already exists)
    s3.upload_file(localFile, bucketName, s3Key)
    print(f"✅ '{localFile}' successfully uploaded to S3 bucket '{bucketName}' as '{s3Key}'")

# Example usage (Replace with actual values)
if __name__ == "__main__":
    # I usually keep my data backups in S3, so this is useful
    uploadFileToS3('nba_stats.csv', 'hoopmetrics-data', 'nba/stats-latest.csv')

    # This could be used for logs or anything else I want stored in the cloud
    uploadFileToS3('game_logs.txt', 'hoopmetrics-data', 'logs/game-logs.txt')
