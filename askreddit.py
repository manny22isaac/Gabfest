#/Users/ammanuelisaac/Desktop/Gabfest/askreddit

import praw, random, pprint
#line4-7 are what allow a user to send a client request to reddit's servers.
#to use the API you need to have a reddit account.
#line 8 will return a Boolean Value if the request came through.

reddit = praw.Reddit(client_id='',
                             client_secret='',
                             user_agent='')
print(reddit.read_only)
#the amount of subreddits.
subreddits = ['AskReddit',\
                      'AskMen',\
                      'AskWomen']

submissions = ['controversial',\
                  'new',\
                  'top',\
                  'gilded',\
                  'hot',\
                  'rising']

#if a title has a curse word in the title the program will pass it in line 39
curseWords = []

#this list will also pass questions in askReddit form
redditFormatQuestions = ['AskReddit', 'askreddit']

#selects a random subreddit from the subreddit list
secure_Random = random.SystemRandom()


#this will select one of the string variables at random
#then it will make the call the the server with the variable reddit as the client id

age = int(input("Please enter your age. --> "))
if age < 18:
    for submission in reddit.subreddit(secure_Random.choice(subreddits)).new(limit=5):
        if str(curseWords) in submission.title:
            pass
        pprint.pprint(submission.title)
else:
    for submission in reddit.subreddit(secure_Random.choice(subreddits)).new(limit=5):
        if str(redditFormatQuestions) in submission.title:
            pass
        pprint.pprint(submission.title)
