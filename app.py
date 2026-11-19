"""Starter example created with AI assistance. Customize and test it yourself."""
import streamlit as st
from planner import split_minutes

st.set_page_config(page_title="Session Splitter", page_icon="⏱")
st.title("Session Splitter")
st.write("Divide your available time into simple practice or work blocks.")
st.caption("Learning demo. No AI API, accounts, or saved user records.")

with st.form("session"):
    minutes = st.number_input("Available minutes", min_value=1, max_value=180, value=25, step=1)
    activities = st.number_input("Number of activities", min_value=1, max_value=12, value=3, step=1)
    submitted = st.form_submit_button("Split my time")

if submitted:
    try:
        blocks = split_minutes(int(minutes), int(activities))
    except ValueError as error:
        st.warning(str(error))
    else:
        st.table({"Activity": list(range(1, len(blocks) + 1)), "Minutes": blocks})
        st.success(f"Total planned: {sum(blocks)} minutes")

st.caption("Next experiment: reserve five minutes for a break. Predict the new results first.")
