# Bot for reddit and shit, fuck cooldownbot lmao...
import os
import praw
import argparse
import time

# Made by Flyingcar12

CLIENTID = ("")
CLIENTSECRET = ("") # fill in all the blanks to make this work
CLIENTUSER = ("")
CLIENTPASS = ("")

print('  ')
print(' FuckThisShitBot41, hope this works...')
print(" ███████╗██╗   ██╗ ██████╗██╗  ██╗████████╗██╗  ██╗██╗███████╗███████╗██╗  ██╗██╗████████╗██████╗  ██████╗ ████████╗██╗  ██╗ ██╗")
print(" ██╔════╝██║   ██║██╔════╝██║ ██╔╝╚══██╔══╝██║  ██║██║██╔════╝██╔════╝██║  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝██║  ██║███║")
print(" █████╗  ██║   ██║██║     █████╔╝    ██║   ███████║██║███████╗███████╗███████║██║   ██║   ██████╔╝██║   ██║   ██║   ███████║╚██║")
print(" ██╔══╝  ██║   ██║██║     ██╔═██╗    ██║   ██╔══██║██║╚════██║╚════██║██╔══██║██║   ██║   ██╔══██╗██║   ██║   ██║   ╚════██║ ██║")
print(" ██║     ╚██████╔╝╚██████╗██║  ██╗   ██║   ██║  ██║██║███████║███████║██║  ██║██║   ██║   ██████╔╝╚██████╔╝   ██║        ██║ ██║")
print(" ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝        ╚═╝ ╚═╝")
print(" [searching...]")

parser = argparse.ArgumentParser(description="Reply to cooldownbot's comments")
parser.add_argument('--reply', dest='reply',
                    help='Reply to target comments with this phrase')
args = parser.parse_args()
reply = args.reply
# reddit instance
reddit = praw.Reddit(client_id=(CLIENTID),
                     client_secret=(CLIENTSECRET),
                     user_agent='Reddit bot tutorial v0.1-1',
                     username=(CLIENTUSER),
                     password=(CLIENTPASS))

for submission in reddit.redditor('CoolDownBot').stream.submissions():
    x = 1
    while x < 6:
        submission.reply(reply)
        time.sleep(6)
        # my output
        print(f" Replied to {submission.author.name}! ({submission.id}) in [{submission.subreddit}]")
        # made it so that it shows the person youre replying to, basically to prevent fuck ups again (Yes, again lol)
        
            
            
