import psutil
import smtplib
import json
import time
from classes.clsConfig import Configuration
import datetime
from twilio.rest import Client
import os
from functions.functionLibrary import *
import time
import threading 
import schedule

""" Victor Ifezue
    Professor Tom Petz
    Week 9 Assignment

    I used the schedule module to schedule the report to be sent.
    I also used threading for the text message alerts

    INSTRUCTION TO RUN EVERY MINUTE*****
    This will run every 60 seconds because of the while loop and sleep(60). 
    I know I didnt create a doc but I wanted to leave this Flowerbox with the instructions for credit.
"""




#gets the configuration from JSON and loads into class
myConfig = getConfiguration()


#sets a schedule for report to run
schedule.every().day.at("06:00").do(reportFeature)
schedule.every().day.at("18:00").do(reportFeature)

programRunning = True
while programRunning:
    try:
        schedule.run_pending()
        #runs the text message alerts feature
        textMessageFeature(myConfig)
        #waits 60 seconds before it runs again
        time.sleep(60)
    except Exception as error:
        print(error)
        time.sleep(60)
        pass

