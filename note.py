import streamlit as st
import pyperclip

# File to store notes
notesFile = "notes.txt"

# Function to add a note
def add_note(note):
    with open(notesFile, "a") as file:
        file.write(note + "\n")

# Function to list notes
def list_notes():
    with open(notesFile, "r") as file:
        return file.readlines()

# Function to remove a note
def remove_note(note):
    notes = list_notes()
    notes.remove(note)
    with open(notesFile, "w") as file:
        for n in notes:
            file.write(n)
            
def copyNote(note):
	pyperclip.copy(note)

def search_notes(keyword):
	all_notes = list_notes()
	found_notes = []
	for note in all_notes:
		if keyword.lower() in note.lower():
			found_notes.append(note)
	return found_notes

# Streamlit UI
def main():
    st.title("Notepad")

    # Sidebar for adding notes
    with st.sidebar:
        st.header("Add Note")
        note_input = st.text_area("Enter your note:")
        if st.button("Add"):
            if note_input:
                add_note(note_input)
                st.success("Note added successfully!")
            else:
                st.warning("Please enter a note!")
        #search notes
        st.header("Search Notes")
        search_input = st.text_input("Enter keyword:")
        if st.button("Search"):
        	if search_input:
        		search_results = search_notes(search_input)
        		if search_results:
        			st.success("Notes found:")
        			for note in search_results:
        				st.write(note)
        		else:
        			st.info("No notes found.")
        	else:
        		st.warning("Please enter a keyword to search.")


    # Main content to list, edit, and delete notes
    st.header("Your Notes")
    all_notes = list_notes()
    if all_notes:
    	i = 1
    	for note in (all_notes):
            st.write("%d. %s" % (i, note))
            
            col1, col2 = st.columns(2)
            with col2:
            	# Delete option
            	if st.button("Delete Note %d" % (i)):
            		remove_note(note)
            		st.success("Note deleted successfully!")
            i += 1
    else:
    	st.write("No notes added yet.")

main()

import streamlit as st
import pyperclip

# File to store notes
notesFile = "notes.txt"

# Function to add a note
def add_note(note):
    with open(notesFile, "a") as file:
        file.write(note + "\n")

# Function to list notes
def list_notes():
    with open(notesFile, "r") as file:
        return file.readlines()

# Function to remove a note
def remove_note(note):
    notes = list_notes()
    notes.remove(note)
    with open(notesFile, "w") as file:
        for n in notes:
            file.write(n)

# Function to copy a note to clipboard
def copy_note(note):
    pyperclip.copy(note)

# Function to search notes based on keyword
def search_notes(keyword):
    all_notes = list_notes()
    found_notes = []
    for note in all_notes:
        if keyword.lower() in note.lower():
            found_notes.append(note)
    return found_notes

# Streamlit UI
def main():
    st.title("Notepad")

    # Sidebar for adding notes
    with st.sidebar:
        st.header("Add Note")
        note_input = st.text_area("Enter your note:")
        if st.button("Add"):
            if note_input:
                add_note(note_input)
                st.success("Note added successfully!")
            else:
                st.warning("Please enter a note!")

        # Search notes
        st.header("Search Notes")
        search_input = st.text_input("Enter keyword:")
        if st.button("Search"):
            if search_input:
                search_results = search_notes(search_input)
                if search_results:
                    st.success("Notes found:")
                    for note in search_results:
                        st.write(note)
                else:
                    st.info("No notes found.")
            else:
                st.warning("Please enter a keyword to search.")

    # Main content to list and delete notes
    st.header("Your Notes")
    all_notes = list_notes()
    if all_notes:
        i = 1
        for note in all_notes:
            st.write("%d. %s" % (i, note))
            col1, col2 = st.columns([3, 1])
            with col2:
                # Delete option
                if st.button("Delete Note %d" % (i)):
                    remove_note(note)
                    st.success("Note deleted successfully!")
            i += 1
    else:
        st.write("No notes added yet.")

if __name__ == "__main__":
    main()
