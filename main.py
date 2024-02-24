import info
import requests
import json
from taiga import TaigaAPI

api = TaigaAPI(host="https://board.nyampass.com")
api.auth(
    username=info.username,
    password=info.password,
)
token = api.token

def post(to,data):
    requests.post(
        url="https://board.nyampass.com/api/v1/"+to,
        headers={'Authorization': 'Bearer {}'.format(api.token)},
        data=data
    )
def patch(to,data):
    requests.patch(
        url="https://board.nyampass.com/api/v1/"+to,
        headers={'Authorization': 'Bearer {}'.format(api.token)},
        data=data
    )

# post("userstories",{"_attrs":{"project":2,"subject":"","description":"","tags":[],"points":{},"swimlane":3,"status":7,"is_archived":False},"_name":"userstories","_dataTypes":{},"_modifiedAttrs":{"subject":"Request Test"},"_isModified":True,"project":2,"subject":"Request Test","description":"Hey","tags":[],"points":{},"swimlane":3,"status":7,"is_archived":False,"is_closed":False})
# post("tasks",
#     {"subject":"Task Test from Requests","assigned_to":None,"status":6,"project":2,"user_story":127}
# )
# status: 7 9 10 11 12
patch("userstories/125",{"status":8,"version":12})

# requests.post(
#     url="https://board.nyampass.com/api/v1/userstories",
#     headers={
#         'Authorization': 'Bearer {}'.format(api.token)
#     },
#     data={"_attrs":{"project":2,"subject":"","description":"","tags":[],"points":{},"swimlane":3,"status":7,"is_archived":False},"_name":"userstories","_dataTypes":{},"_modifiedAttrs":{"subject":"Request Test"},"_isModified":True,"project":2,"subject":"Request Test","description":"Hey","tags":[],"points":{},"swimlane":3,"status":7,"is_archived":False,"is_closed":False}
# )



# resp = requests.post(
#     url="https://board.nyampass.com/api/v1/auth",
#     data={
#         "password":info.password,
#         "type":"normal",
#         "username":info.username
#     },
#     headers={"Content-Type":"application/json"}
# )
# print(resp.status_code)
# print(vars(resp))