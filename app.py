import sys
from config import DB_DETAILS

def main():
    #for arg in sys.argv:
     env = sys.argv[1]
     db_details = DB_DETAILS[env]
     print(db_details)
if __name__ == '__main__':
    main()

####run -> config add db user & db pass