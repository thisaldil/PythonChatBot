import streamlit as st
import openai
import time

# Set your OpenAI API key
openai.api_key = "##"

# Initialize the messages list with a system message
messages = [{"role": "system", "content": "You are a financial expert that specializes in Business and negotiation"}]

def get_chat_response(user_input):
    # Append the user's input to the messages list
    messages.append({"role": "user", "content": user_input})
    
    while True:
        try:
            # Create a response using the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            chat_reply = response["choices"][0]["message"]["content"]
            # Append the assistant's reply to the messages list
            messages.append({"role": "assistant", "content": chat_reply})
            return chat_reply
        
        except openai.error.RateLimitError:
            st.write("Rate limit exceeded. Retrying after 5 minutes...")
            time.sleep(300)
        
        except openai.error.AuthenticationError:
            st.write("Invalid API key. Please check your API key.")
            return
        
        except openai.error.APIError as e:
            st.write(f"OpenAI API error occurred: {e}")
            return
        
        except Exception as e:
            st.write(f"An unexpected error occurred: {e}")
            return

# Streamlit UI
st.title("AI-Powered ChatBot   ")

# Input text box for user messages
user_input = st.text_input("You:", "")

# Button to send the message
if st.button("Send"):
    if user_input:
        # Get the response from the chatbot
        response = get_chat_response(user_input)
        # Display the response
        st.write(f"**Assistant:** {response}")

