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

openai.api_key = os.getenv('GPT_TOKEN')

def handle_response(message):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = message,
        temperature = 0.1,
        max_tokens = 1024,
        )
    responseMessage = response.choices[0].text

    return responseMessage