#environment declaration 

# Program Name: 
# Programer Name 
# Version
# Date
#
# Program Function:
#

# Import Libraries
import praw
import argparse
from r_credit_class import reddit_keys


# Variable Initilization 
#
#
parser = argparse.ArgumentParser(description='This will retreave reddit posts and text from the chosen redditlist. -s is a required field. Howerver, default count is 1 if -c is not used')
parser.add_argument('-subreddit' , metavar='<subreddit>' , type=str , required=True, help='subreddit to add')
parser.add_argument('-cnt' , metavar='c' , type=int , default='1' , help='Number of posts to list')

args = parser.parse_args()

reddit = praw.Reddit(client_id= reddit_keys['client_id'],
                     client_secret= reddit_keys['client_secret'], password= reddit_keys['password'],
                     user_agent= reddit_keys['user_agent'], username= reddit_keys['username'])

# Function Definition 
#
#	
class PostClass():

    def __init__(self, dict_post, sub):
        #self.posts = dict_posts
        self.subr = sub 
        self.Title = dict_post['Title']
        self.ID = dict_post['ID']
        self.isStickied = dict_post['Stickied']
        self.Score = dict_post['Score']
        self.upv = dict_post['UpvoteR']
        self.no_com = dict_post['No_com']
        self.Url = dict_post['Url']
        self.link = dict_post['Link']
        self.Text = dict_post['Text']

    def get_sreddit(self):
        return self.subr
    def get_title(self):
        return self.Title
    def get_subID(self):
        return self.ID
    def get_stick_status(self):
        return self.isStickied
    def get_score(self):
        return self.Score
    def get_upvotes(self):
        return self.upv
    def get_commentNo(self):
        return self.no_com
    def get_link1(self):
        return self.Url
    def get_link2(self):
        return self.link
    def get_PostBody(self):
        return self.Text

    
    def dis_post_title(self):
        print('{} '.format(self.Title))

    def dis_post_ID_and_title(self):
        print('{}\t\t\t{}'.format(self.ID, self.Title))

    def dis_post_title_by_id(self, posts, id_in):
        for s in posts.values():
            if id_in == s: 
                self.dis_post_title_and_text()
            else:
                return



    def dis_post_stats(self):
        print('Subreddit: {}\t PostId: {}\tPost Score {}\tNo of Comments= {}\nUrl: {}\nLink: {}'.format(self.subr, self.ID,self.Score,self.no_com,self.Url,self.link))

    def dis_post_title_and_text(self):
        self.dis_post_title()
        print('\n')
        if self.Text != '':
            print('{}'.format(self.Text))
        else:
            self.dis_post_stats()


    def get_post_IDs(self):
        pids = []

        pids.append(self.ID)
        return pids
        

        

#Program Logic 
#
#
sub_posts = {}
sub_posts_ids = []
print('\n\t\t *******{}********\n'.format(args.subreddit))
for submission in reddit.subreddit(args.subreddit).new(limit=args.cnt):

    sub_posts = {'Title': submission.title, 'ID':submission.id, 'Stickied':submission.stickied, 'Score':submission.score, 'UpvoteR':submission.upvote_ratio, 'No_com':submission.num_comments, 'Url':submission.url, 'Link':submission.permalink, 'Text':submission.selftext }

    my_posts = PostClass(sub_posts, args.subreddit)
    sub_posts_ids.append(my_posts.ID)

    for i in sub_posts_ids:
        print(i)


'''    print('Sub: {}\n Title: {}\n ID: {}\n Stickied: {}\n Score: {}\n UpVotes: {}\n No. Comments: {}\n Link: {}\n Link2: {}\n'.format(my_posts.get_sreddit(),my_posts.get_title(),my_posts.get_subID(),my_posts.get_stick_status(),my_posts.get_score(),my_posts.get_upvotes(),my_posts.get_commentNo(),my_posts.get_link1(),my_posts.get_link2()))


    if args.cnt == 1 and my_posts.isStickied == 'True':
        pass
    elif args.cnt == 1:
        my_posts.dis_post_title_and_text()
    else:
        my_posts.dis_post_ID_and_title()
        #print('{}'.format(len(sub_posts_ids)))
'''
g_id = input('get id from user: ') 
if g_id in sub_posts_ids:
    #print('You have entered id: {}, we have {}'.format(g_id,sub_posts_ids))
    for index, value in enumerate(sub_posts_ids):
        if value == g_id:
            print('{}'.format(value))
            print('{}'.format(my_posts.dis_post_title_by_id(sub_posts, value)))
else:
    print('There is no match for {}'.format(g_id))

for key, value in sub_posts.items():
    if value == g_id:
        my_posts.dis_post_title_by_id(sub_posts, value)
    else:
        print('none found')
    #print('{} {}'.format(sub_posts['ID'], sub_posts['Title']))

# start of main 
#
# 
