import requests
import json

auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQWRtaW4iLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxIiwicHJpbWFyeXNpZCI6InRlc3QiLCJ1bmlxdWVfbmFtZSI6ImFkbWluIiwianRpIjoiNTBmMWY0MjMtNjQ5NC00ZjcxLWJkZTctNTNkOGZmZjE4NzM2IiwibmJmIjoxNjI4MDYwNzU4LCJleHAiOjE2Mjg2NjU1NTgsImlhdCI6MTYyODA2MDc1OH0.f1wsQyBw_0cyIsWbMOHxO4Jd5e4ZbRCfR0YgVgu0M64'
header = {
    'Authorization': 'Bearer ' + auth_token,
    'content-type': 'application/json'
}

# data = {
#             "term": "babbitt",
#             "entryDefinitionsList": {
#                 "definition": [
#                     "to line, face, or furnish with Babbitt metal. "
#                 ],
#                 "usage": [
#                     ""
#                 ],
#                 "entryClassification": {
#                     "classificationName": "verb (used with object)"
#                 }
#             }
#         }

data = {
    "status": 1,
    "languageId": 1,
    "term": "Computer",
    "termClassificationId": 1,
    "origin": "English",
    "definition": "A non-portable computing device",
    "usage": "Let's code on your computer",
    "linkedTermId[]": ""
}

data = json.dumps(data)

endpoint = '/api/v1/Terms/AddNew'
url = 'http://dictionary.arjun.com.np'
endpoint = f'{url}{endpoint}'

response = requests.post(endpoint, data=data, headers=header)
print(response)
# print(response.json())