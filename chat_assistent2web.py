import openai
import gradio as gr
import time

# Set your OpenAI API key
openai.api_key = "sk-tSgw_a_AmEhPE82UYGDmtJJgz-CODjqBTUGA9WkKq7T3BlbkFJ3pc1YwVpFPIA8JaALM64i4T05bk6up3_pr5Es2pRQA"

# Initial system message to set the assistant's role
messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    # Append the user's input to the messages
    messages.append({"role": "user", "content": user_input})
    
    while True:
        try:
            # Create a response using the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            # Extract the assistant's reply from the response
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            # Append the assistant's reply to the messages
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            return ChatGPT_reply
        
        except openai.error.RateLimitError:
            # If rate limit is exceeded, wait for 5 minutes before retrying
            print("Rate limit exceeded. Retrying after 5 minutes...")
            time.sleep(300)
        
        except openai.error.AuthenticationError:
            # If there is an authentication error, print an error message and break the loop
            print("Invalid API key. Please check your API key.")
            break
        
        except openai.error.APIError as e:
            # If there is an API error, print the error message and break the loop
            print(f"OpenAI API error occurred: {e}")
            break
        
        except Exception as e:
            # If an unexpected error occurs, print the error message and break the loop
            print(f"An unexpected error occurred: {e}")
            break

# Create a Gradio interface for the custom ChatGPT function
demo = gr.Interface(
    fn=CustomChatGPT,  # The function to be called for each input
    inputs="text",  # Input type is text
    outputs="text",  # Output type is text
    title="Real Estate Pro"  # Title of the Gradio interface
)

# Launch the Gradio interface with sharing enabled
demo.launch(share=True)
