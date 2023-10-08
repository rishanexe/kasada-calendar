import streamlit as st
from streamlit_calendar import calendar

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
calendar_events = [
    {
        "title": "UI\/UX Project Proposal Final",
        "start": "2022-09-27 10:00:00",
        "end": "2022-09-27 11:00:00"
    },
    {
        "title": "UI\/UX assignment solution modification discussion",
        "start": "2022-10-01 10:00:00",
        "end": "2022-10-01 10:30:00"
    },
    {
        "title": "UI\/UX Project Survey Questions",
        "start": "2022-10-09 19:30:00",
        "end": "2022-10-09 20:30:00"
    },
    {
        "title": "UI\/UX Project Survey Questions Cont...",
        "start": "2022-10-10 13:30:00",
        "end": "2022-10-10 14:30:00"
    },
    {
        "title": "Initial Discussion",
        "start": "2022-10-30 19:00:00",
        "end": "2022-10-30 20:00:00"
    },
    {
        "title": "FW: Data Challenge Workshop: How to speak Data",
        "start": "2022-11-04 11:00:00",
        "end": "2022-11-04 12:00:00"
    },
    {
        "title": "Software Dev Project Initializaton",
        "start": "2022-11-07 19:00:00",
        "end": "2022-11-07 20:00:00"
    },
    {
        "title": "FW: Data Challenge 2022",
        "start": "2022-11-18 07:00:00",
        "end": "2022-11-18 15:30:00"
    },
    {
        "title": "FW: Data Challenge 2022 Panel Discussion",
        "start": "2022-11-18 11:15:00",
        "end": "2022-11-18 12:15:00"
    },
    {
        "title": "Heuristic Evaluation changes documentation",
        "start": "2022-11-20 20:30:00",
        "end": "2022-11-20 21:30:00"
    },
    {
        "title": "Tax Return Information Session for International Students",
        "start": "2023-02-27 16:00:00",
        "end": "2023-02-27 17:00:00"
    },
    {
        "title": "Rishan Mascarenhas and Trishla Shah",
        "start": "2023-04-19 14:45:00",
        "end": "2023-04-19 15:15:00"
    },
    {
        "title": "Historic test appointment",
        "start": "2023-10-06 00:00:00",
        "end": "2023-10-07 00:00:00"
    },
    {
        "title": "Test Appointment",
        "start": "2023-10-10 08:00:00",
        "end": "2023-10-10 08:30:00"
    }
]

calendar = calendar(events=calendar_events, options=calendar_options)
# st.write(calendar)