import streamlit as st
from streamlit_calendar import calendar
import json
import requests
from cryptography.fernet import Fernet

# Calendar page
def calendar_view():
    calendar_options = {
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridDay,dayGridWeek,dayGridMonth",
        },
        "slotMinTime": "08:00:00",
        "slotMaxTime": "20:00:00",
        "initialView": "dayGridWeek",
    }

    # Load key
    payload = {"key": st.secrets["API_KEY"]}
    headers = {'Content-type': 'application/json'}
    r = requests.post('https://kasada.pythonanywhere.com/get-events', json=payload, headers=headers)
    calendar_events = r.json()

    # DECRYPT
    fernet = Fernet(st.secrets["CRYPTO_KEY"])
    calendar_events = fernet.decrypt(calendar_events["data"].encode("utf-8")).decode("utf-8")
    calendar_events = json.loads(calendar_events)

    # Render the calendar view
    calendar_view = calendar(events=calendar_events[0], options=calendar_options)

    st.write(f"Updated on: {calendar_events[1]['updated_on']}")
