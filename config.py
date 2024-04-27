import os

API_ID = API_ID = 27506873

API_HASH = os.environ.get("API_HASH", "a6e35f157348c804affcadece912fd30")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7154988164:AAHq_msn_DImidUdTwyQdF-muMGq4T6TgBw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6518807195)

LOG = -1002052344384

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-1002052344384').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6518807195 ").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


