import win32com.client
from dateutil.parser import *
import pandas as pd

# Access Outlook and get the events from the calendar
Outlook = win32com.client.Dispatch("Outlook.Application")
ns = Outlook.GetNamespace("MAPI")
appts = ns.GetDefaultFolder(9).Items

# Sort events by occurence and include recurring events
appts.Sort("[Start]")
appts.IncludeRecurrences = "True"

# Populate dictionary of meetings
apptDict = []
for a in appts:
    start_date = parse(str(a.Start))
    end_date = parse(str(a.End))

    apptDict.append({
        "title": str(a.Subject),
        "start": start_date.strftime("%Y-%m-%d %H:%M:%S"),
        "end": end_date.strftime("%Y-%m-%d %H:%M:%S"),
    })

# Convert dictionary to dataframe
apt_df = pd.DataFrame(apptDict)

# Save to json
apt_df.to_json("data/calendar.json", orient='records')
