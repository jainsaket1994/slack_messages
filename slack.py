from slackclient import SlackClient
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"] 

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):

    slack_client = SlackClient(SLACK_TOKEN)
    api_call = slack_client.api_call("im.list")

    user_slack_id = "U5ZCT3D53"

    with open('message.txt','r') as f:
        message = f.read()

    if api_call.get('ok'):
        for im in api_call.get("ims"):
            if im.get("user") == user_slack_id:
                im_channel = im.get("id")
                slack_client.api_call("chat.postMessage", channel=im_channel, text=message, as_user=True)
                                      
                                        
    s.enter(2, 1, do_something, (sc,))

s.enter(2, 1, do_something, (s,))
s.run()
