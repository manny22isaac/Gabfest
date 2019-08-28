#/Users/ammanuelisaac/Desktop/Gabfest/askreddit

import praw, random, time, sys

reddit = praw.Reddit(client_id='',
                             client_secret='',
                             user_agent='')
print(reddit.read_only)


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
submissions = ['controversial',\
                      'new',\
                      'top',\
                      'gilded',\
                      'hot',\
                      'rising']

curseWords = ['CurseWords go here.']

redditFormatQuestions = ['AskReddit',\
                             'askreddit',\
                             'reddit',\
                             'Reddit',\
                             'of Reddit',\
                             'of reddit']



class Gabfest():

    #and the stored variables from in the class Gabfest sent to the init functions parameters using the self method to store the variables

    def __init__(self, name, age, filters):

        self.name = name
        self.age = age
        self.filters = filters

    # if a users age is below 18 it will pass any reddit post containing adult content. Otherwise it will return a question.
    # the type of posts can be altered by the # of questions a user wants and what types of reddit titles

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


#allows a user to enter in their name age and subreddit topics.
#The program will print out the titles of the available subreddit topics.

name = input("Please enter your name: ")
age = input("Welcome " + name + ". Please enter your age: ")

all_subreddits = ['AskMen','AskWomen','AskReddit','whowouldwin','explainlikeimfive']

print("""Below are the subreddits you can recieve questions from.
      You may use up to 5 subreddit\'s.
      Please copy and paste the titles in the response below: """)

for i in range(len(all_subreddits)):
    print(all_subreddits[i])

#allows a user to copy and paste the subreddit into the input
#and fill up the list saved a the variable filters which will be used as a parameter
#or it will end the program by leaving the input blank.

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
#sends the parameters (name, age, filters) provided by the user to the Class Gabfest as a local variable
#takes the varible person1 and send the GET requests to reddit.

person1 = Gabfest(name, age, filters)
person1.questionGet()
