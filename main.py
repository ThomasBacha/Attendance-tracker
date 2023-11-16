import streamlit as st
import random
import pandas as pd
import datetime

# Mock function for user authentication and data update
def user_login(username, password):
    return username == "user1" and password == "password123"

def update_user_data(users, user, date):
    users[user]["points"] += 10
    users[user]["badges"].append("Attendance Badge")
    users[user]["attendance"].append(date)  # Storing the date directly

# Initialize Streamlit App
st.set_page_config(page_title="Gamified Attendance System", layout="wide")

# User data initialization
users = {
    "user1": {"points": 0, "badges": [], "attendance": []}
}

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
            st.metric("Points", users[user_selected]["points"])
        with col2:
            st.metric("Badges", len(users[user_selected]["badges"]))

        # Calendar and Attendance Registration
        st.subheader("Mark Your Attendance")
        attendance_date = st.date_input("Select Date", datetime.date.today())
        if st.button("Mark Attendance"):
            update_user_data(users, user_selected, attendance_date)
            st.success("Attendance Marked for " + str(attendance_date))

        # Plotting Attendance Patterns
        st.subheader("Attendance Patterns")
        if users[user_selected]["attendance"]:
            df = pd.DataFrame(users[user_selected]["attendance"], columns=["Date"])
            df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
            df['Day'] = df['Date'].dt.day_name()    # Now you can use dt accessor
            attendance_count = df['Day'].value_counts()

            # Using Streamlit's native chart functionality
            st.bar_chart(attendance_count)
        else:
            st.write("No attendance data to display.")

        # Display User Data
        st.subheader("Your Achievements")
        st.write(f"Points: {users[user_selected]['points']}")
        st.write(f"Badges: {', '.join(users[user_selected]['badges'])}")

        # Activity History
        st.subheader("Your Activity History")
        st.write("Attendance Dates: " + ', '.join(str(date) for date in users[user_selected]["attendance"]))

# Footer
st.sidebar.write("Gamified Attendance System © 2023")
