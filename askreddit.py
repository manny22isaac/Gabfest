import praw, random


reddit = praw.Reddit(client_id='<client_id>',
                     client_secret='<client_secret>',
                     user_agent='Gabfest(Prototype)')

print(reddit.read_only)

subreddit = ['AskReddit','NoStupidQuestions','WouldYouRather','explainlikeimfive']

secure_Random = random.SystemRandom()
for submission in reddit.subreddit(secure_Random.choice(subreddit)).new(limit=1):
    print(submission.title)
