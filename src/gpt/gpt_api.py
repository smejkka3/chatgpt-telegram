# import os
# import openai
# from loguru import logger
    
# class GPT:
#     def __init__(self):
#         openai.api_key = os.environ.get('GPT_TOKEN')
#         logger.info("Authenticated...") 
        
        
#     def ask_question(self, question):     
#         logger.info(openai.api_key)   
#         response = openai.Completion.create(
#             engine = "text-davinci-003",
#             prompt = question,
#             temperature = 0.6,
#             max_tokens = 150,
#             )
#         return response.choices[0].text

import os
import openai

from revChatGPT.Official import Chatbot
from asgiref.sync import sync_to_async
from env import GPT_TOKEN

openai.api_key = GPT_TOKEN

def handle_response(message):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = message,
        temperature = 0.1,
        max_tokens = 4096,
        )
    responseMessage = response.choices[0].text

    return responseMessage