import yaml
import datetime as dt
import info #ログイン用の個人のパスワード、ユーザ名を入れてあります
import requests
from taiga import TaigaAPI
import json

api = TaigaAPI(host="https://board.nyampass.com")
api.auth(
    username=info.username,
    password=info.password,
)
token = api.token

def post(to,data):
    return requests.post(
        url="https://board.nyampass.com/api/v1/"+to,
        headers={'Authorization': 'Bearer {}'.format(api.token)},
        data=data
    )
def patch(to,data):
    return requests.patch(
        url="https://board.nyampass.com/api/v1/"+to,
        headers={'Authorization': 'Bearer {}'.format(api.token)},
        data=data
    )

def passed(target):
    now = dt.datetime.now()
    time = target.split()
    return (dt.datetime(now.year,int(time[3]),int(time[2]),int(time[1]),int(time[0])) - now).days<0
    # min h day month weekday

with open('tasks2.yaml') as file:
    tasks = yaml.full_load(file)["tasks"]
    for task in tasks:
        if "title" in task:
            if passed(task["cron"]):
                res = post("userstories",{"_attrs":{"project":2,"subject":"","description":"","tags":[],"points":{},"swimlane":3,"status":7,"is_archived":False},"_name":"userstories","_dataTypes":{},"_modifiedAttrs":{"subject":task["title"]},"_isModified":True,"project":2,"subject":task["title"],"description":"Hey","tags":[],"points":{},"swimlane":3,"status":7,"is_archived":False,"is_closed":False})
                if "sub_tasks" in task:
                    ID = json.loads(res._content.decode())["id"]
                    for subtask in task["sub_tasks"]:
                        post("tasks",{"subject":subtask["title"],"assigned_to":None,"status":6,"project":2,"user_story":ID})
        elif "type" in task:
            if task["type"] == "archive":
                if passed(task["cron"]):
                    print("ok")