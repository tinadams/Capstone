###################################################################################################
# Tessa Adams
# timer.py
# Program that works as a timer and gives alerts when task is complete
# 5/8/24
###################################################################################################

#import
import streamlit as st
import time
from plyer import notification

# Function to read tasks from the text file
def readTasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to write a single task to the text file
def writeTask(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

# Function to rewrite all tasks to the text file (used for deleting tasks)
def rewriteTasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to delete a task from the text file
def deleteTask(task):
    tasks = readTasks()
    if task in tasks:
        tasks.remove(task)
    rewriteTasks(tasks)

# Function to send a notification
def sendNotification(task):
    notification.notify(
        title="Timer",
        message=task,
        timeout=10  # Notification timeout in seconds
    )

def main():
    st.title("Timer")
    st.write("Enter your task below:")

    text = st.text_input("Task:")
    minutes = st.number_input("In how many minutes?", min_value=1)

    if st.button("Set Task"):
        if text:  # Ensure that the text input is not empty
            writeTask(text)
            st.write(f"Task '{text}' is set for {minutes} minutes.")
            # Use Streamlit's progress bar and sleep in a non-blocking way
            with st.spinner(f"Waiting for {minutes} minutes..."):
                time.sleep(minutes * 60)
            st.success(f"Time's up for task: {text}")
            sendNotification(text)
            deleteTask(text)

    # Sidebar for listing tasks
    with st.sidebar:
        st.header("Your Tasks")
        tasks = readTasks()
        if tasks:
            for task in tasks:
                st.write(task)
        else:
            st.write("No tasks set yet.")

if __name__ == "__main__":
    main()
