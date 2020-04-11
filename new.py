import praw
import time

reddit = praw.Reddit(client_id="",
                        client_secret="",
                        user_agent='',
                        username="",
                        password="")
print(reddit.read_only)


def spam():
    try:
        for comment in reddit.redditor('cooldownbot').comments.new(limit=None):
            comment.reply("fuck")
    except:
        print("ratelimit")
        time.sleep(60000)
        spam()

spam()
