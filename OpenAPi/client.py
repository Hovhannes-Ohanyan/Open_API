from openai import OpenAI
import json
import take_json


def create_class():
    scrapped_json = take_json.get_json()

    client = OpenAI(
        api_key="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")

    prompt = (f"Generate a Python class to handle API calls based on the Swagger JSON:\n"
              f"{scrapped_json}\n\n")
    prompt += "Our class should have methods like 'health_check()', 'post_whisper_task(audio_url, whisper_model, language)', and 'get_whisper_output(transaction_id)'.\n"
    prompt += "_base_url = 'custom url'\n\n"
    prompt += 'also in __init__ function we must have headers'
    prompt += '/gw1/whisper/v1/health before all endpoints must be added /gw1'
    prompt += "self.headers = {'x-app-authorization': api_key} header must be like this.\n"
    prompt += "The output should be string that I can pass to exec() function."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.0,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": prompt}
        ]
    )
    return list(json.loads(response.choices[0].message.content).values())[0]
