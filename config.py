import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","MOTU_PATALU_HINDU_HAI")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "MOTU_PATLU_HINDU_MUSI_VCBOT)
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "MOTU PATLU HINDU MUSIC BOT")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "MOTU_PATLU_HINDU_MUSI_VCBOT)
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ajaybabu69f:XF0vwerJ7QuyYJGS@cluster0.1vop5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002372170981)
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7886419837))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Shuaib6869/ROSEXMSUIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MRMOTUPATLUCHAT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MRMOTUPATLUCHAT")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQAf70YAuU0w2ihZwP47FdiDu3cM-11dllsdwZYVHHtImukb2ZkZg1KiWaZLqSdP17mrfib5hRcDx80oxsnDHF6Hxh_597rC7re5Kroml-TxfEQzYck1lFGM59qP-DP1B_YXuQz5F8gVrlZ10pUMGrCTdmAJddrXnkkF3PpzHZVivNgTR4WJzG6LGITea_YWQz9PQusqai0IFdFXekBXwY4mG_3xE9ycXOjXPWwPI7z6ssYttKho3213gbl4B-Rtp4QNvYpb8ZSEVFw49gtfnVEMOzbmr1zbJVOgV9Y5s6dA_dSFEUfu8yTJ2sIlKmXIL2Qp4ySYJfpQagfnh5mcsAdrsWLCSAAAAAGqLuGNAAskn_pnH3v7qJbIY2dh2WfxHg4-psD8oxPbN_zdETQwnDat08haMDtT_okPQXGFBrWluH_9pYqcsU6i80jfUs96ril0Olpih9HlHQSva2jRut6oKxN-s7SUbH40gAAAAHmzJyYAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://ibb.co/bRqFn2B2"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://ibb.co/bRqFn2B2"
)
PLAYLIST_IMG_URL = "https://ibb.co/bRqFn2B2"
STATS_IMG_URL = "https://ibb.co/bRqFn2B2"
TELEGRAM_AUDIO_URL = "https://ibb.co/bRqFn2B2"
TELEGRAM_VIDEO_URL = "https://ibb.co/bRqFn2B2"
STREAM_IMG_URL = "https://ibb.co/bRqFn2B2"
SOUNCLOUD_IMG_URL = "https://ibb.co/bRqFn2B2"
YOUTUBE_IMG_URL = "https://ibb.co/bRqFn2B2"
SPOTIFY_ARTIST_IMG_URL = "https://ibb.co/bRqFn2B2"
SPOTIFY_ALBUM_IMG_URL = "https://ibb.co/bRqFn2B2"
SPOTIFY_PLAYLIST_IMG_URL = "https://ibb.co/bRqFn2B2"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
