#HoopMetrics - NBA Analytics Dashboard
#Author: Fady Youssef
#Description: This script fetches NBA player data from an API and processes it for analysis.


from api.nba_api import APIPlayerData
import datetime

def main():
    # Timestamp for when the script is run
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"HoopMetrics Data - {currentTime}")

    # Fetch player data
    players = APIPlayerData()
    
    if players:
        print(f"Successfully fetched {len(players)} players from the API.")
    else:
        print("No players found. Check API response.")

if __name__ == '__main__':
    main()
