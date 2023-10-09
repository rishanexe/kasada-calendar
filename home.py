import streamlit as st
from streamlit_calendar import calendar
import json

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
        "initialView": "dayGridMonth",
    }

    # Load all events in calendar data
    with open('data/calendar.json') as file:
        calendar_events = json.load(file)

    # Render the calendar view
    calendar_view = calendar(events=calendar_events, options=calendar_options)
