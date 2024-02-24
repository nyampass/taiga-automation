import yaml

def compare(now):
    return

with open('test.yaml') as file:
    tasks = yaml.full_load(file)["tasks"]
    for task in tasks:
        if "title" in task:
            print("Title Run")
        elif "type" in task:
            if task["type"] == "archive":
                print("Archived")