import streamlit as st
from data_handler import update_user_data, user_login
import datetime
import pandas as pd

# Initialize Streamlit App
st.set_page_config(page_title="Gamified Attendance System", layout="wide")

# User data initialization
users = {
    "user1": {"points": 0, "badges": [], "attendance": []}
}

# Session state for data persistence
if 'users' not in st.session_state:
    st.session_state['users'] = users

# For demonstration, assuming user is always authenticated
st.session_state['authenticated'] = True
st.session_state['current_user'] = "user1"

# Main Dashboard
if st.session_state.get('authenticated', False):
    user_selected = st.session_state['current_user']
    with st.container():
        st.title(f"Welcome, {user_selected}")

        # Dashboard Layout
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Points", st.session_state['users'][user_selected]["points"])
        with col2:
            st.metric("Badges", len(st.session_state['users'][user_selected]["badges"]))

        # Calendar and Attendance Registration
        st.subheader("Mark Your Attendance")
        attendance_date = st.date_input("Select Date", datetime.date.today())
        if st.button("Mark Attendance"):
            update_user_data(st.session_state['users'], user_selected, attendance_date)
            st.success("Attendance Marked for " + str(attendance_date))

        # Plotting Attendance Patterns
        st.subheader("Attendance Patterns")
        if st.session_state['users'][user_selected]["attendance"]:
            df = pd.DataFrame(st.session_state['users'][user_selected]["attendance"], columns=["Date"])
            df['Date'] = pd.to_datetime(df['Date'])  # Ensure dates are datetime objects
            df['Day'] = df['Date'].dt.day_name()
            attendance_count = df['Day'].value_counts()

            # Using Streamlit's native chart functionality
            st.bar_chart(attendance_count)
        else:
            st.write("No attendance data to display.")

        # Display User Data
        st.subheader("Your Achievements")
        st.write(f"Points: {st.session_state['users'][user_selected]['points']}")
        st.write(f"Badges: {', '.join(st.session_state['users'][user_selected]['badges'])}")

        # Activity History
        st.subheader("Your Activity History")
        st.write("Attendance Dates: " + '\n'.join(str(date) for date in st.session_state['users'][user_selected]["attendance"]))

# Footer
st.sidebar.write("Gamified Attendance System © 2023")
