import streamlit as st
from streamlit_calendar import calendar
import json

calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridDay,dayGridWeek,dayGridMonth",
    },
    "slotMinTime": "08:00:00",
    "slotMaxTime": "20:00:00",
    "initialView": "dayGridMonth",
}

with open('data/calendar.json') as f:
    calendar_events = json.load(f)

calendar = calendar(events=calendar_events, options=calendar_options)
# st.write(calendar)
