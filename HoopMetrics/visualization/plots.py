
import matplotlib.pyplot as plt
import pandas as pd
import boto3
import json

# Load player data from S3 and create visualizations
def loadPlayerData(bucket, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(obj['Body'].read())
    return pd.DataFrame(data['players'])

def plotTopScorers(bucket, key):
    df = loadPlayerData(bucket, key)
    top_scorers = df.sort_values(by='points', ascending=False).head(5)
    plt.figure(figsize=(8, 5))
    plt.bar(top_scorers['name'], top_scorers['points'], color='blue')
    plt.xlabel("Player")
    plt.ylabel("Points Per Game")
    plt.title("Top 5 Scorers")
    plt.show()

def plotAssistsVsRebounds(bucket, key):
    df = loadPlayerData(bucket, key)
    plt.figure(figsize=(8, 5))
    plt.scatter(df['assists'], df['rebounds'], c='green', alpha=0.5)
    plt.xlabel("Assists Per Game")
    plt.ylabel("Rebounds Per Game")
    plt.title("Assists vs. Rebounds")
    plt.show()

#update with real bucket and key
# plotTopScorers('bucket', 'players.json')
# plotAssistsVsRebounds('bucket', 'players.json')
