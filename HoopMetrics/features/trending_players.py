import json
import boto3

def getTrendingPlayers(bucket, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(obj['Body'].read())
    return sorted(data['players'], key=lambda x: x['points'], reverse=True)[:5]