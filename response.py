from datetime import datetime
import openai
import requests
import json
import os

#api_key = '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'

def resp(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hi","hello"):
        return "Hi, I am Aishwarya. My Master LORD NIRAJ created me!!!"
    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return date_time
    else:

        
        api_key = ('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')

        # Set the OpenAI API key
        openai.api_key = api_key
        complete = openai.Completion.create(engine='text-davinci-003', prompt = user_message, max_tokens = 100)
        return complete.choices[0]['text']
        
        
        
    return "Didn't Understand"