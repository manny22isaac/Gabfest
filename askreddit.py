#/Users/ammanuelisaac/Desktop/Gabfest/askreddit

import praw, random, time, sys

reddit = praw.Reddit(client_id='',
                             client_secret='',
                             user_agent='')
print(reddit.read_only)


secure_Random = random.SystemRandom()

#--------------------------------------------------------#
    #selects a random subreddit from the subreddit list
secure_Random = random.SystemRandom()

#--------------------------------------------------------#
    #the amount of subreddits.
subreddits = ['AskReddit',\
                          'AskMen',\
                          'AskWomen']
all_subreddits = []
#--------------------------------------------------------#
#this lists are used in the lines 52-67
submissions = ['controversial',\
                      'new',\
                      'top',\
                      'gilded',\
                      'hot',\
                      'rising']
curseWords = ['sex',\
                  'NSFW',\
                  'fuck',\
                  'shit',\
                  'ass',\
                  'dick',\
                  'cunt',]

redditFormatQuestions = ['AskReddit',\
                             'askreddit',\
                             'reddit',\
                             'Reddit',\
                             'of Reddit',\
                             'of reddit']



class Gabfest():


    def __init__(self, name, age, filters):

        self.name = name
        self.age = age
        self.filters = filters


    def questionGet(self):
        if int(self.age) < 18:
            for submission in reddit.subreddit(secure_Random.choice(self.filters)).new(limit=5):
                if str(curseWords) and str(redditFormatQuestions) in submission.title:
                    pass
            print(self.name + ', Here is your question. ' + submission.title)

        else:
            for submission in reddit.subreddit(secure_Random.choice(self.filters)).new(limit=5):
                if str(redditFormatQuestions) in submission.title:
                    pass
                print(self.name + ', Here is your question. ' + submission.title)

        return True



name = input("Please enter your name: ")
age = input("Welcome " + name + ". Please enter your age: ")

all_subreddits = ['AskMen','AskWomen','AskReddit','whowouldwin','explainlikeimfive']

print("""Below are the subreddits you can recieve questions from.
      You may use up to 5 subreddit\'s.
      Please copy and paste the titles in the response below: """)

for i in range(len(all_subreddits)):
    print(all_subreddits[i])

filters = []
print('Enter a subreddit topics below. When finished, hit enter to continue the program.')
while True:
    print('Paste the subreddit here. Hit enter to leave the program: ')
    reddit_titles = input()
    if reddit_titles == '':
        break
    filters = filters + [reddit_titles]
    if len(filters) == 5:
        print("Subreddit's have been selected.")
        break

person1 = Gabfest(name, age, filters)
person1.questionGet()
