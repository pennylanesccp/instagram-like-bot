from main import *
from encrypt import *

INSTAGRAM_USERNAME = "felipesaproenca"
INSTAGRAM_PASSWORD = main()
TARGET_USERNAME_LIST = [
    "patiza1609"
    , "isagumierolee"
    , "1casamentoperfeito"
]
n=0

for TARGET_USERNAME in TARGET_USERNAME_LIST:
    like_bot(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, TARGET_USERNAME, n)
