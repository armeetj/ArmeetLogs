import json
import datetime
from git import Repo
import time 

PATH_OF_GIT_REPO = r'.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = ''
TODAY_DATE =str(datetime.date.today())
print("date: " + TODAY_DATE)
print("enter message for today: ")
message = input()

#confirmation
print("date: " + TODAY_DATE)
print("message: " + message)
print("confirm? (y) or (n): ")

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(["."])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

if(input() == 'y'):
    git_push()
    print("success! closing in 5 seconds...")
    time.sleep(5);
    exit();
else:
    print("cancelled, stopping in 5 seconds...")
    time.sleep(5);
    exit();