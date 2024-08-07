import openai
import time

# Set your OpenAI API key
openai.api_key = "##"

# List to store the conversation messages
messages = []

# Get the initial system message from the user to set the assistant's role
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while True:
    try:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if the user types 'quit()'
        if user_input.lower() == "quit()":
            print("Ending the chat. Goodbye!")
            break

        # Append the user's message to the messages list
        messages.append({"role": "user", "content": user_input})

        # Create a response using the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract and print the assistant's reply
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("\nAssistant: " + reply + "\n")

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
