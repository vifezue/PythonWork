
import platform
import json
import os.path
import datetime
import ezsheets
import smtplib
import psutil
from classes.clsConfig import Configuration
from twilio.rest import Client
import threading 
import time

def sendReportEmail(myConfig, message):
    """
    Sends the report email
    """
    smtpConn = smtplib.SMTP(myConfig.mail_server, myConfig.mail_port)
    smtpConn.ehlo()
    smtpConn.starttls()
    smtpConn.login(myConfig.username, myConfig.password)
    my_message = """"From: victor@starfishtechandlearning.com
    Subject: Report Details
    """ + "\n" + str(message)
    smtpConn.sendmail(myConfig.from_email, myConfig.to_email, my_message)
    smtpConn.close()


def getConfiguration():
    """
    Gets the configuration from the JSON response
    """
    jsonPath = os.path.join("text_files", "script_config.json")

    with open(jsonPath) as json_file:
        data = json.load(json_file)

        mail_server = str(data['mail_server'])
        mail_port = int(data['mail_port'])
        password = data['password']
        username = data['username']
        from_email = data['from_email']
        to_email = data['to_email']
        twilio_account_id = data['twilio_account_id']
        twilio_auto_token = data['twilio_auto_token']
        twilio_trial_number = data['twilio_trial_number']
        twilio_cell_number = data['twilio_cell_number']
        last_text = data['last_text']

    myConfig = Configuration(mail_server,
                             mail_port,
                             username,
                             password,
                             from_email,
                             to_email,
                             twilio_account_id,
                             twilio_auto_token,
                             twilio_trial_number,
                             twilio_cell_number,
                             last_text)

    return myConfig


def getCpuUsagePercent():
    """
    Gets CPU useage and returns string percentage
    """
    percent = str(psutil.cpu_percent(interval=.1))
    percent = percent + "%"
    return percent

def getCpuUsagePercentStr():
    """
    Gets CPU useage and returns string percentage for text message alerts
    """
    strValue = getCleanDateTimeStr()
    percent = str(psutil.cpu_percent(interval=.1))
    percent = percent + "%"
    strValue += " - The current CPU use is "+ percent+"."
    return strValue


def getMemoryUsage():
    """
    Gets Memory useage and returns string percentage for text message alerts
    """
    value = psutil.virtual_memory()
    finalValue = str((value[2]))+"%"
    return finalValue


def getDiskUseage():
    """
    Gets Disk useage and returns string percentage
    """
    volumes = psutil.disk_partitions()
    for volume in volumes:
        dataValue = psutil.disk_usage(volume[1])
        value = str(dataValue[3])+"%"
        return value

def getDiskUseageStr():
    """
    Gets Disk useage and returns string percentage for text message alerts
    """
    diskUseageStr = getCleanDateTimeStr()
    volumes = psutil.disk_partitions()
    for volume in volumes:
        valueData = psutil.disk_usage(volume[1])
        diskUseageStr += " - The current disk usage is " + str(valueData[3])+"%"
    return diskUseageStr


def getMemoryUseageStr():
    """
    Gets Memory useage and returns string percentage for text message alerts and reporting
    """
    valueStr = ""
    value = psutil.virtual_memory()
    valueStr = "The available memory is " + str(value[1]) + " bytes.\n"
    valueStr += "The amount of memory that was used is " + \
        str(value[3]) + " bytes.\n"
    valueStr += "The percentage of memory used is " + str(value[2]) + " %.\n"
    return valueStr

def memoryUseageStr():
    """
    Gets Memory useage and returns string percentage for text message alerts
    """
    valueStr = getCleanDateTimeStr()
    value = psutil.virtual_memory()
    valueStr += " - The percentage of memory used is " + str(value[2]) + " %."
    return valueStr

def createCPUPercentageString():
    """
    Gets CPU useage and returns string percentage for reporting
    """
    cpuValuesString = ""
    cpuValues = psutil.cpu_percent(interval=.1, percpu=True)
    coreNumber = 1
    for value in cpuValues:
        cpuValuesString += str(value) + " %" + " of core number " + str(
            coreNumber)+" from the " + str(len(cpuValues)) + " are currently in use.\n"
        coreNumber += 1
    return cpuValuesString


def generatePacketStr():
    """
    Gets Packet useage and returns string percentage for reporting
    """
    strValue = ""
    data = psutil.net_io_counters()
    packetsDropped = int(data[6] + int(data[7]))
    inputOutputErrors = int(data[4]+int(data[5]))

    strValue = "The amount of bytes currently being sent is " + \
        str(data[0]) + " packets.\n"
    strValue += "The amount of bytes currently being received is " + \
        str(data[1]) + " packets.\n"
    strValue += "The amount of packets currently being dropped is " + \
        str(packetsDropped) + ".\n"
    strValue += "The amount of input and output errors are " + \
        str(inputOutputErrors) + ".\n"

    return strValue


def generateEmailReport():
    """
    Generate process for the daily report
    """
    reportString = 'Computer Report Details \n'
    today = datetime.today()
    strDate = today.strftime("%b %d, %Y")
    now = datetime.now()
    strTime = now.strftime("%H:%M:%S")
    cleanDateTime = strDate + " " + strTime

    # entered the report created date
    reportString += cleanDateTime + " is the report date.\n\n"

    # entered the CPU stats
    reportString += 'CPU Statistics \n'
    cpuPercentageString = createCPUPercentageString()
    reportString += cpuPercentageString + "\n"

    # enter memory useage stats
    reportString += 'Disk Usage Statistics \n'
    diskUseageStr = getDiskUseageStr()
    reportString += diskUseageStr + "\n\n"

    # enters the memory useage stats
    reportString += 'CPU Statistics \n'
    memUseageStr = getMemoryUseageStr()
    reportString += memUseageStr + "\n"

    # enter the network information
    reportString += 'Network Usage Statistics \n'
    networkUseageStr = generatePacketStr()
    reportString += networkUseageStr

    return reportString


def getCleanDateTimeStr():
    """
    Gets a clean date time string
    """
    today = datetime.date.today()
    strDate = today.strftime("%b %d, %Y")
    now = datetime.datetime.now()
    strTime = now.strftime("%H:%M:%S")
    cleanDateTime = strDate + " " + strTime
    return cleanDateTime


def sendTextMessageAlert(myConfig, message):
    """
    Send a text message and updates the last_text field within the class
    """
    current_time = datetime.datetime.now()
    last_text = myConfig.get_last_text()
    if last_text != '':
        difference = current_time - datetime.strptime(last_text)
        difference_in_seconds = difference.total_seconds()

    if last_text == '' or float(difference_in_seconds) >= 3600.00:    

        accountID = myConfig.twilio_account_id
        authToken = myConfig.twilio_auto_token
        trialNumber = myConfig.twilio_trial_number
        cellNumber = myConfig.twilio_cell_number

        twClient = Client(accountID, authToken)

        my_message = twClient.messages.create(
            body=message, from_=trialNumber, to=cellNumber)

        myConfig.update_last_text(str(current_time))
    else:
        pass


def textMessageFeature(myConfig):
    #Text message FEATURE   
    generateTextMessageAlerts(myConfig)
    time.sleep(3600)
    return

def reportFeature():
    #Report Feature
    myConfig = getConfiguration()
    myReport = generateEmailReport()
    sendReportEmail(myConfig,myReport)
    time.sleep(60)
    return

def diskUseageAlert(myConfig):
    #Disk Useage Alert
    diskUseageValue = float(getDiskUseage().replace("%",""))
    if diskUseageValue > 70.0:
        sendTextMessageAlert(myConfig,getDiskUseageStr())
    else:
        pass

def totalMemoryUseageAlert(myConfig):
    #Total Memory Useage Alert
    memoryUseageValue = float(getMemoryUsage().replace("%",""))
    if memoryUseageValue > 90.00:
        sendTextMessageAlert(myConfig,memoryUseageStr)
    else:
        pass

def cpuUseageAlert(myConfig):
    #CPU Useage Alert
    cpuUseageValue = float(getCpuUsagePercent().replace("%",""))
    if cpuUseageValue > 85.00:
        sendTextMessageAlert(myConfig,getCpuUsagePercentStr())
    else:
        pass

def packetsAlert(myConfig):
    #Packet Useage Alert
    strValue = ""
    data = psutil.net_io_counters()
    packetsDropped = float(data[6] + int(data[7]))
    inputOutputErrors = float(data[4]+int(data[5]))

    if packetsDropped > 0.00 or inputOutputErrors > 0.00:
        packetAlertStr = getCleanDateTimeStr()
        packetAlertStr += " - There are some input output errors and packets dropped."
        sendTextMessageAlert(myConfig,packetAlertStr)       


def generateTextMessageAlerts(myConfig):
    #Text Message Alert Process
    t1 = threading.Thread(target=diskUseageAlert(myConfig),args=myConfig)
    t2 = threading.Thread(target=totalMemoryUseageAlert(myConfig),args=myConfig)
    t3 = threading.Thread(target=cpuUseageAlert(myConfig),args=myConfig)
    t4 = threading.Thread(target=packetsAlert(myConfig),args=myConfig)

    try:
        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
    except:
        print("Text Message Process Failed.")