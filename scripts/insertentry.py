import json

def add_entry(TODAY_DATE, ENTRY_MESSAGE):
    #read file and convert to dict
    logsFile = open('logs.json', 'r+')
    logsFileRaw = logsFile.read()
    pythonLogs = json.loads(logsFileRaw)
    pythonLogs[str(TODAY_DATE.split('-')[0])].append({"date":"hi", "message": "hi"})
    print(pythonLogs)

add_entry("2019-11-27", "test entry")