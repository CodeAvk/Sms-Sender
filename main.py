import requests
import json

def send_msg(number,message):
    url='https://www.fast2sms.com/dev/bulkV2 '
    
    # Creating Dictinoary
    params={
        "authorization":"5yMPCmJIxOLtF49EvD0gbYeswNZq2ncp8QiVRHTdulKhAfBzkW4bEh7pWKz9RSsaf83AUeNj1HBdwTZc",
        "sender_id":"TXTIND", # the sender id may be vary...so make sure that you use correct sender id and you can customize it
        "message":message,
        "language":"english",
        "route":"v3", # use "t" for transaction purpose and "p" for promotion purpose
        "numbers":number

    }
    # Get Request
    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)



send_msg("9937962984","This is avk")
