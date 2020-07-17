import pymysql
import io
import json
import csv
import re
import time
import json
import os.path
import datetime
from utilFunctions.functions import *
from classes.database_access import DB_Connect
from classes.clsDataSet import *

my_db = DB_Connect('root', '', 'python_projects')

# print(":::::Welcome to the Final Destination:::::")
# actionType = getAction()
# print(actionType)
# if actionType == "Import A New Data File":


importJsonFileToDataBase()

