from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("API_KEY_OPENAI")

def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=prompt,
        temperature=0.75,
        max_tokens=2048
    ) 
    return response['choices'][0]['text']

    # response_dict = response.get("choices")
    # if response_dict and len(response_dict) > 0:
    #     prompt_response = response_dict[0]["text"]
    # return prompt_response