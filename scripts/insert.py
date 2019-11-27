import json
import datetime
from git import Repo
import time 

PATH_OF_GIT_REPO = r'.git'  # make sure .git folder is properly configured
TODAY_DATE =str(datetime.date.today())
ENTRY_MESSAGE = '' 

def git_push(COMMIT_MESSAGE):
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(["."])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

def add_entry(TODAY_DATE, ENTRY_MESSAGE):
    #read file and convert to dict
    logsFile = open('logs.json', 'r+')
    logsFileRaw = logsFile.read()
    logsFile = open('logs.json', 'w+')
    pythonLogs = json.loads(logsFileRaw)
    try:
        pythonLogs[str(TODAY_DATE.split('-')[0])].append({"date":TODAY_DATE, "message": ENTRY_MESSAGE})
    except:
        pythonLogs[str(TODAY_DATE.split('-')[0])] = {}
        pythonLogs[str(TODAY_DATE.split('-')[0])].append({"date":TODAY_DATE, "message": ENTRY_MESSAGE})

    logsFile.write(json.dumps(pythonLogs, indent=4, separators=(',', ': ')))

print("ADD ENTRY")
print("================================================")
print("date: " + TODAY_DATE)
print("enter message for today: ")
ENTRY_MESSAGE = input()

print()
#confirmation
print("CONFIRMATION")
print("================================================")
print("date: " + TODAY_DATE)
print("message: " + ENTRY_MESSAGE)
print("confirm? (y) or (n): ")

if(input() == 'y'):
    add_entry(TODAY_DATE, ENTRY_MESSAGE)
    git_push(TODAY_DATE)
    print()
    print("OUTPUT")
    print("================================================")
    print("entry added...")
    print("pushed to git...")
    print("success! closing in 5 seconds...")
    time.sleep(5);
    exit();
else:
    print("OUTPUT")
    print("================================================")
    print("cancelled, stopping in 5 seconds...")
    time.sleep(5);
    exit();