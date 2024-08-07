import openai
import time

# Set your OpenAI API key
openai.api_key = "sk-tSgw_a_AmEhPE82UYGDmtJJgz-CODjqBTUGA9WkKq7T3BlbkFJ3pc1YwVpFPIA8JaALM64i4T05bk6up3_pr5Es2pRQA"

def get_openai_response(messages):
    while True:
        try:
            # Create a response using the OpenAI API
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            # Extract and return the assistant's reply from the response
            return completion.choices[0].message.content
        
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

# Define the initial message from the user
messages = [{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis"}]

# Get the response from the OpenAI API
response = get_openai_response(messages)

# Print the response if it exists
if response:
    print(response)
