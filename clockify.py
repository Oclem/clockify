#/usr/bin/python3

## START
# curl -H "content-type: application/json" -H "X-Api-Key: KEY" -X POST https://api.clockify.me/api/v1/workspaces/WORKSPACE_ID/time-entries -d '{"start":"2020-04-03T22:46:38.220223Z","billable":"false","description":"test api","projectId":"5bd886a6b07987515be9737a"}'

## END
# curl -H "content-type: application/json" -H "X-Api-Key: KEY" -X PATCH https://api.clockify.me/api/v1/workspaces/WORKSPACE_ID/user/USER_ID/time-entries -d '{"end":"2020-04-03T22:59:21.347230Z"}'

## TIME
# datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
import datetime
import argparse
import sys

time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
projectid = "5bd886a6b07987515be9737a" # Développement
api_key = os.environ['CLOCKIFY_KEY']
api_key_head = {'X-Api-Key': api_key}
r = requests.get("https://api.clockify.me/api/v1/user",headers=api_key_head, verify=False)
rdict = r.json()
workspaceid = rdict['activeWorkspace']
userid = rdict['id']
start_url = "https://api.clockify.me/api/v1/workspaces/"+workspaceid+"/time-entries"
end_url = "https://api.clockify.me/api/v1/workspaces/"+workspaceid+"/user/"+userid+"/time-entries"

def start_timer(description): 
  dataz = {"start":time,"billable":"false","description":description,"projectId":projectid}
  r = requests.post(start_url, headers=api_key_head, verify=False, json=dataz)
  print(r.json())

def end_timer(): 
  dataz = {"end":time}
  r = requests.patch(end_url, headers=api_key_head, verify=False, json=dataz)
  print(r.json())

def interval_timer(start_time,end_time,description): 
  start = datetime.datetime(start_time).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
  end = datetime.datetime(end_time).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
  dataz = {"start":start,"billable":"false","description":description,"projectId":projectid,"end":end}
  r = requests.post(start_url, headers=api_key_head, verify=False, json=dataz)
  print(r.json())

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', help="Start timer", action='store_true')
  parser.add_argument('-e', help="End timer", action='store_true' )
  parser.add_argument('-d', help="Description",required='-s' in sys.argv)
  parser.add_argument('-i', help="Set interval: -s and -e required in utc format", action='store_true')
  parser.add_argument('-S', help="Start time for interval",required='-i' in sys.argv)
  parser.add_argument('-E', help="End time for interval",required='-i' in sys.argv)
  args = parser.parse_args()

  start = args.s
  end = args.e
  description = args.d
  interval = args.i
  start_time = args.S
  end_time = args.E

  if start: 
    start_timer(description)
  if end:
    end_timer()
  if interval:
    if '-d' in sys.argv:
      interval_timer(start_time,end_time,description)
    else:
      print('-d is required') # pas trouvé comment required pour deux args

main()
