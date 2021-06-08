import os

class var(object):
  OWNER_ID = int(os.environ.get("OWNER_ID", None))
  BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
  API_HASH = os.environ.get("API_HASH", None)
  APP_ID = int(os.environ.get("APP_ID", 6))
  DB_URL = os.environ.get("DATABASE_URL", None)
