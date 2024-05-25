import instaloader
import requests
import time

INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""
TARGET_USERNAME = input("Enter the target username: ")

if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD or not TARGET_USERNAME:
    print("Please set the INSTAGRAM_USERNAME, INSTAGRAM PASSWORD and TARGET_USERNAME variables.")
    exit()

L = instaloader.Instaloader()
