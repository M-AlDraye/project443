import requests
import json

URL = "http://localhost:8088/api/v1/namespaces/default/pods/"

resp = requests.get(url=URL)
resp_json = json.loads(resp.content)
pods = resp_json["items"]

pod_num = 1
for pod in pods:
    name = pod["metadata"]["name"]
    uid = pod["metadata"]["uid"]
    print("Pods",pod_num,":\nName:" , name , "\nUID:" , uid , "\n")
    pod_num+=1