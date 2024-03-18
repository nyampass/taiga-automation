import yaml
import datetime as dt
from taiga import TaigaAPI
from dotenv import load_dotenv
load_dotenv()
import os

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
project = os.getenv("PROJECT")
default_swimlane = os.getenv("DEFAULT_SWIMLANE")
host = os.getenv("HOST")
database_path = os.getenv("DATABASE_PATH")

api = TaigaAPI(host=host)
api.auth(
    username=username,
    password=password,
)
projects = api.projects.get_by_slug(project)
swimlanes = {i.name : i.id for i in projects.list_swimlanes()}
statuses = {i.name : i.id for i in projects.list_user_story_statuses()}
users = {i.username:i.id for i in api.users.list()}
task_id = api.task_statuses.list()[0].id
userstories = projects.list_user_stories()

def passed(target,current=None):
    now = dt.datetime.now() if current==None else current
    time = target.split()
    diff = (dt.datetime(now.year,int(time[3]),int(time[2]),int(time[1]),int(time[0])) - now).total_seconds()
    return ((diff<=0) and (diff/60>=-30))
    # min h day month weekday

with open(database_path) as file:
    tasks = yaml.full_load(file)["tasks"]
    for task in tasks:
        if passed(task["cron"]):
            if "title" in task:
                swim = swimlanes[task["swim"]] if "swim" in task and task["swim"] in swimlanes else swimlanes[default_swimlane]
                assign = users[task["assign"]] if "assign" in task and task["assign"] in users else None
                new = projects.add_user_story(task["title"],description="",swimlane=swim,assigned_to=assign)
                print("task created.")
                if "sub_tasks" in task:
                    for sub_task in task["sub_tasks"]:
                        new.add_task(sub_task["title"],status=task_id)
            elif "type" in task:
                if task["type"] == "archive":
                    done = list(filter(lambda e:e.status==statuses["Done"],userstories))
                    for i in done:
                        i.update(swimlane=swim,status=statuses["Archived"])
