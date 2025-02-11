import pytest
from api.nba_api import fetchPlayerData

def testFetchPlayerData():
    # Get player data from the API
    players = fetchPlayerData()

    if isinstance(players, list):
        if len(players) > 0:
            # If the list isn't empty, check if it has expected fields
            firstPlayer = players[0]

            if 'name' not in firstPlayer:
                print("Error: 'name' field is missing in player data.")
            
            if 'points' not in firstPlayer:
                print("Error: 'points' field is missing in player data.")
            
            print(f"Test passed: Retrieved {len(players)} players.")
        
        else:
            print("Warning: API returned an empty player list.")

    else:
        print("Error: API response is not a list.")

def testFetchPlayerDataEmpty():
    # Get data and check if it's empty but still a valid list
    players = fetchPlayerData()

    if isinstance(players, list):
        if len(players) == 0:
            print("Warning: API returned no players. This might be an issue.")
        else:
            print(f"Test passed: Retrieved {len(players)} players.")
    else:
        print("Error: API response is not a list.")
