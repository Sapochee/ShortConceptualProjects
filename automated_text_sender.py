""" Sends an automated text message once a day - can make another file with phone numbers to import for confidentiality
"""

import requests
import schedule
import time

phoneNumber = "Any# Here"

def send_message():
    resp = requests.post('https://textbelt.com/text', 
                         {'phone' : phoneNumber,
                         'message' : "Good Morning, I hope you have a good day",
                         'key' : 'textbelt'
                         })
    print(resp.json())
    
schedule.every().day.at('08:00').do(send_message)
      
while True:
    schedule.run_pending()
    time.sleep(1)