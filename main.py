import instaloader
import requests
import time

def like_post(post):
    post_url = f"https://www.instagram.com/web/likes/{post.mediaid}/like/"
    response = session.post(post_url)
    if response.status_code == 200:
        print(f"Liked post: {post.shortcode}")
    else:
        print(f"Failed to like post: {post.shortcode}, Status code: {response.status_code}")

def like_bot(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, TARGET_USERNAME, n=0):
    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD or not TARGET_USERNAME:
        print("Please set the INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, and TARGET_USERNAME variables.")
        exit()

    L = instaloader.Instaloader()
    L.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    profile = instaloader.Profile.from_username(L.context, TARGET_USERNAME)
    session = L.context._session

    if n == 0:
        posts = profile.get_posts()
    else:
        posts = profile.get_posts()[0:n]

    for post in posts:
        like_post(post)
        time.sleep(30)

    print(f"Liked all posts of user: {TARGET_USERNAME}")
