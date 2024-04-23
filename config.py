import os

API_ID = API_ID = 28842408

API_HASH = os.environ.get("API_HASH", "af9694549d2521e43db424978a39cf03")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6797355310:AAGZozwQ9s1sClMWGTU3zEeU1YG_ksDxMm0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6368210712)

LOG = -1002024624642

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-1002024624642').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6368210712 ").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


