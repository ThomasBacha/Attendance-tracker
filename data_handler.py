import random
import pandas as pd
import datetime

# Mock function for user authentication
def user_login(username, password):
    return username == "user1" and password == "password123"

# Function to update user data
def update_user_data(users, user, date):
    users[user]["points"] += 10
    users[user]["badges"].append("Attendance Badge")
    users[user]["attendance"].append(date)  # Storing the date directly
