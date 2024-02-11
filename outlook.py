import win32com.client, datetime
from dateutil.parser import *
from datetime import date
import pandas as pd
from cryptography.fernet import Fernet
import logging
import requests
import json

logging.basicConfig(filename='data/log.log', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', level=logging.INFO)


def run():
    # Access Outlook and get the events from the calendar
    logging.info("Access Outlook and get the events from the calendar")
    Outlook = win32com.client.Dispatch("Outlook.Application")
    ns = Outlook.GetNamespace("MAPI")
    appts = ns.GetDefaultFolder(9).Items

    # Sort events by occurence and include recurring events
    logging.info("Sort events by occurence and include recurring events")
    appts.Sort("[Start]")
    appts.IncludeRecurrences = "True"

    # Filter date range
    logging.info("Filter date range")
    begin = date.today() - datetime.timedelta(days=30)
    begin = begin.strftime("%m/%d/%Y")
    end = date.today() + datetime.timedelta(days=60)
    end = end.strftime("%m/%d/%Y")
    appts = appts.Restrict(f"[Start] >= '{begin}' AND [END] <= '{end}'")

    # Populate dictionary of meetings
    logging.info("Populate dictionary of meetings")
    apptDict = [[]]
    for a in appts:
        start_date = parse(str(a.Start))
        end_date = parse(str(a.End))

        apptDict[0].append({
            "title": str(a.Subject),
            "start": start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "end": end_date.strftime("%Y-%m-%d %H:%M:%S"),
        })

    # Updated timestamp
    apptDict.append({"updated_on": datetime.datetime.now().strftime("%d %b %Y at %I:%M:%S %p")})

    # Convert list to json    
    data = json.dumps(apptDict)

    # Save to json
    logging.info("Save to json file")
    with open('data/calendar.json','w') as f:
        f.write(data)

    # ---------- ENCRYPTION --------------
    logging.info("ENCRYPTION")

    with open('crypto_key.key','rb') as file:
        crypto_key = file.read()

    fernet = Fernet(crypto_key)
    encrypted = fernet.encrypt(data.encode("utf8"))

    # Post to API
    logging.info("Post to API")
    with open('api_key.key','r') as file:
        api_key = file.read()

    payload = {"key": str(api_key), "data": encrypted.decode("utf8")}
    headers = {'Content-type': 'application/json'}
    r = requests.post('https://kasada.pythonanywhere.com/update-events', json=payload, headers=headers)
    print(r.text)

    # Save encrypted data to JSON
    logging.info("Save encrypted data to JSON")
    with open('data/calendar_encrypted.json','wb') as f:
        f.write(encrypted)

    logging.info("------------------ DONE ------------------")


if __name__ == '__main__':
    try:
        run()
    except Exception as err:
        logging.exception(str(err))