import boto3
from configparser import ConfigParser

def s3Config(filename='config/s3_config.ini', section='aws'):
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    return config

def s3Upload(file_name, bucket, object_name=None):
    config = s3Config()
    s3 = boto3.client('s3', aws_access_key_id=config['aws_access_key_id'], aws_secret_access_key=config['aws_secret_access_key'], region_name=config['region'])
    if not object_name:
        object_name = file_name
    s3.upload_file(file_name, bucket, object_name)
    print(f"Uploaded {file_name} to S3 bucket {bucket} as {object_name}")

# Example usage
if __name__ == "__main__":
    s3Upload('sample.txt', 'your_bucket', 'sample_upload.txt')
