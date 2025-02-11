import boto3
from configparser import ConfigParser

# Load my S3 credentials from a config file (standard practice for keeping secrets out of code)
def loadS3Config(filename='config/s3_config.ini', section='aws'):
    parser = ConfigParser()
    parser.read(filename)
    s3Config = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            s3Config[param[0]] = param[1]

    return s3Config

# Upload a file to my S3 bucket (make sure AWS credentials are correct)
def uploadToS3(localFile, bucketName, s3Key=None):
    creds = loadS3Config()

    # Set up the S3 client using stored credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=creds['aws_access_key_id'],
        aws_secret_access_key=creds['aws_secret_access_key'],
        region_name=creds['region']
    )

    # If no custom S3 key is provided, just use the filename
    if not s3Key:
        s3Key = localFile

    # Upload file to S3 (this will overwrite if it already exists)
    s3.upload_file(localFile, bucketName, s3Key)
    print(f"✅ '{localFile}' uploaded to S3 bucket '{bucketName}' as '{s3Key}'")

# Example usage (Replace with actual file and bucket)
if __name__ == "__main__":
    # Storing latest player stats in S3
    uploadToS3('player_stats.json', 'hoopmetrics-storage', 'data/player_stats.json')

    # Uploading game logs to S3 for analysis
    uploadToS3('game_logs.csv', 'hoopmetrics-storage', 'logs/game_logs.csv')
