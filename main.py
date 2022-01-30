import requests
import json

def send_msg(number,message):
    url='https://www.fast2sms.com/dev/bulkV2 '
    params={
        "authorization":"5yMPCmJIxOLtF49EvD0gbYeswNZq2ncp8QiVRHTdulKhAfBzkW4bEh7pWKz9RSsaf83AUeNj1HBdwTZc",
        "sender_id":"TXTIND",
        "message":message,
        "language":"english",
        "route":"v3",
        "numbers":number

    }
    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)



send_msg("9937962984","This is avk")