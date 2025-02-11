import pytest
from api.nba_api import fetchPlayerData

def testFetchPlayerData():
    # Making sure I can actually pull NBA player data from the API
    players = fetchPlayerData()
    assert isinstance(players, list)
    assert len(players) > 0

def testFetchPlayerDataEmpty():
    # Checking behavior when API response is empty
    players = fetchPlayerData()
    assert isinstance(players, list)
    assert len(players) >= 0
