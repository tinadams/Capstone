from openai import OpenAI
import streamlit as st

st.title("brAIn buddy")
st.subheader("chat bot")

client = OpenAI(api_key="hi")

if "openai_model" not in st.session_state:
	st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

if prompt := st.chat_input("Say something!"):
	st.session_state.messages.append({"role": "user", "content": prompt})
	with st.chat_message("user"):
		st.markdown(prompt)

	with st.chat_message("assistant"):
		stream = client.chat.completions.create(
			model=st.session_state["openai_model"],
			messages=[
				{"role": m["role"], "content": m["content"]}
				for m in st.session_state.messages
			],
			stream=True,
		)
		response = st.write_stream(stream)
	st.session_state.messages.append({"role": "assistant", "content": response})


from openai import OpenAI
import streamlit as st

# Function to initialize OpenAI client
def initialize_openai_client():
    return OpenAI(api_key="your_api_key_here")

# Function to handle user interaction and chat messages
def handle_chat(messages, client):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Say something!"):
        messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        messages.append({"role": "assistant", "content": response})

# Streamlit UI
def main():
    st.title("brAIn buddy")
    st.subheader("Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    client = initialize_openai_client()
    handle_chat(st.session_state.messages, client)

if __name__ == "__main__":
    main()
