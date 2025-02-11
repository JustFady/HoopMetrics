from database.db_setup import createTables
from api.nba_api import APIPlayerData

def main():
    # Initialize database and fetch player data
    createTables()
    players = APIPlayerData()
    print(f"Fetched {len(players)} players.")

if __name__ == '__main__':
    main()
