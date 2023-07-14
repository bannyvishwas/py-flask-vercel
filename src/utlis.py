import os
import requests
import json
from datetime import datetime
from src.__version__ import version

last_log_date = datetime.now().date()

def rotate_logs_file(filename,cur_date):
    global last_log_date
    cur_date = cur_date.date()
    if last_log_date != cur_date:
        last_log_date = cur_date
        # Rename files
        os.rename(filename,filename.replace(".log",f"-{cur_date}.log"))

def write_logs(log_type,data):
    if log_type == "ERROR":
        file_name = './logs/error/errors.log'
    else:
        file_name = './logs/output/access.log'
    
    current_time = datetime.now()
    rotate_logs_file(file_name,current_time)
    content = f"[{log_type}] :: {current_time} :: {data}\n"
    with open(file_name,"a") as file:
        file.write(content)

def get_success_message(message):
    resp = {
        "status" : True,
        "version" : version,
        "message" : message
    }
    return json.dumps(resp)

def get_error_message(message):
    resp = {
        "status" : False,
        "version" : version,
        "message" : message
    }
    return json.dumps(resp)