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
OWNER_USERNAME = getenv("OWNER_USERNAME","LEGEND_HU_BSDK")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Sikha_music_robot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "SIKHA MUSIC")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Sikha_music_robot")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002265875332))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 6238720068))
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
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VILLAIN_MUSIC_UPDATE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/pardhan_ki_haveli")
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
STRING1 = getenv("STRING_SESSION", "BQE7c0IAk4AYm8dwqVSx3_mbvfEdF31VjSLzRW_C8_hBLDnlVnjII1VZEnFWWNYczj6TYVIHCrqt61WPXl576wQUgnJk_7p26dSFwEJEQ9l-bR8VbHRFaKiJA11l67TxgXXJeX_ze6UUOtMJEBNLhuyDqvKKzs1HFwNCbunYYFjVR5Ran5TP-rDCK6jti3C2LdF4ZOQYpTUMCpmTN919uaMKh-DwZQ7n-hdskn_pnH3v7qJbIY2dh2WfxHg4-psD8oxPbN_zdETQwnDat08haMDtT_okPQXGFBrWluH_9pYqcsU6i80jfUs96ril0Olpih9HlHQSva2jRut6oKxN-s7SUbH40gAAAAHmzJyYAA")
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
    "START_IMG_URL", "https://ibb.co/wQYFctN"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://ibb.co/wQYFctN"
)
PLAYLIST_IMG_URL = "https://ibb.co/wQYFctN"
STATS_IMG_URL = "https://ibb.co/wQYFctN"
TELEGRAM_AUDIO_URL = "https://ibb.co/wQYFctN"
TELEGRAM_VIDEO_URL = "https://ibb.co/wQYFctN"
STREAM_IMG_URL = "https://ibb.co/wQYFctN"
SOUNCLOUD_IMG_URL = "https://ibb.co/wQYFctN"
YOUTUBE_IMG_URL = "https://ibb.co/wQYFctN"
SPOTIFY_ARTIST_IMG_URL = "https://ibb.co/wQYFctN"
SPOTIFY_ALBUM_IMG_URL = "https://ibb.co/wQYFctN"
SPOTIFY_PLAYLIST_IMG_URL = "https://ibb.co/wQYFctN"

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
