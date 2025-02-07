import streamlit as st
import time
from datetime import datetime, timedelta
from plyer import notification

# Function to read reminders from the text file
def read_reminders():
    try:
        with open("reminders.txt", "r") as file:
            reminders = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        reminders = []
    return reminders

# Function to write reminders to the text file
def write_reminder(reminders):
    with open("reminders.txt", "w") as file:
        for reminder in reminders:
            file.write(reminder + "\n")

# Function to remove a reminder from the text file
def remove_reminder(reminders, index):
    del reminders[index]
    write_reminder(reminders)

# Function to process reminders
def process_reminders():
    current_datetime = datetime.now()
    reminders = read_reminders()
    for reminder in reminders:
        reminder_datetime = datetime.strptime(reminder.split("|")[0].strip(), "%Y-%m-%d %H:%M")
        if current_datetime < reminder_datetime:
            time_to_wait = (reminder_datetime - current_datetime).total_seconds()
            time.sleep(time_to_wait)
            notify(reminder.split("|")[1].strip())  # Notify with the reminder message

# Function to display desktop notification
def notify(message):
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10  # Notification timeout in seconds
    )

# Function to convert input time to datetime object
def get_reminder_datetime(date, hours, minutes):
    reminder_datetime = datetime.combine(date, datetime.min.time())
    reminder_datetime = reminder_datetime.replace(hour=hours, minute=minutes)
    return reminder_datetime

# Main function to define Streamlit UI components
def main():
    st.title("Reminder App")
    st.write("Enter your reminder below:")

    text = st.text_input("Reminder:")
    reminder_date = st.date_input("Select date:")
    hours = st.number_input("Enter hours (0-23):", min_value=0, max_value=23, value=0)
    minutes = st.number_input("Enter minutes (0-59):", min_value=0, max_value=59, value=0)

    if st.button("Set Reminder"):
        reminder_datetime = get_reminder_datetime(reminder_date, hours, minutes)
        reminders = read_reminders()
        reminders.append(f"{reminder_datetime.strftime('%Y-%m-%d %H:%M')} | {text}")
        write_reminder(reminders)
        st.write(text)

    # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        reminders = read_reminders()
        if reminders:
            for idx, reminder in enumerate(reminders, start=1):
                reminder_date, reminder_text = reminder.split("|")
                reminder_datetime = datetime.strptime(reminder_date.strip(), "%Y-%m-%d %H:%M")
                st.write(f"Reminder {idx}: {reminder_text.strip()} | {reminder_datetime.date()} | {reminder_datetime.time()}")
                col1, col2, col3 = st.columns([3, 3, 3])
                with col3:
                    if st.button(f"Delete {idx}"):
                        remove_reminder(reminders, idx - 1)
        else:
            st.write("No reminders set yet.")

# Entry point for executing the script
if __name__ == "__main__":
    main()
    process_reminders()  # Only call process_reminders() when script is executed directly
