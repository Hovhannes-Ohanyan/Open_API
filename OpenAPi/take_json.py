import requests
import re


def get_json():
    url = "https://ai.picsart.com/whisper/swagger#/"
    response = requests.get(url)
    json_url_match = re.search(
        r"url:\s+'([^']+/openapi\.json)'", response.text)
    matched_text = json_url_match.group()
    return f"https://ai.picsart.com{matched_text[6:-1]}"
