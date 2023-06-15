import os
import openai
import pprint
from dotenv import load_dotenv
load_dotenv()

def send_and_receive(messages):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

def message_loop(initial_messages):
    message = initial_messages
    while True:
        # send message and receive response
        completion = send_and_receive(message)
        # isolate the response
        response = completion['choices'][0]['message']['content']
        # print the response
        print(response)
        # add the response to the message list
        message.append({'role': 'assistant', 'content': response})
        # get user input
        new_message = input('User: ')
        # add the user input to the message list
        message.append({'role': 'user', 'content': new_message})

def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]

    #define system message
    system_message = {'role':'system'}
    system_message['content'] = input("System: ")

    #define user message
    user_message = {'role':'user'}
    user_message['content'] = input("User: ")

    #define message list
    messages = [system_message, user_message]

    #start message loop
    message_loop(messages)

    


if __name__ == '__main__':
    main()