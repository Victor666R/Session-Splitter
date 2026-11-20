import streamlit as st
from planner import split_minutes

blocks = split_minutes(int(total_minutes), int(activity_count))

# Label activities 1..N, and label the last item as "Break"
rows = []
for i, minutes in enumerate(blocks):
    if i < len(blocks) - 1:
        label = f"Activity {i + 1}"
    else:
        label = "Break"
    rows.append({"Activity": label, "Minutes": minutes})

st.table(rows)
st.success(f"Total planned: {sum(blocks)} minutes (includes 5 min break)")
