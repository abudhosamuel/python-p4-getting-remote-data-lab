import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Return the raw content as a byte string
        response = requests.get(self.url)
        return response.content  # Return the response as bytes

    def load_json(self):
        # Convert the response to JSON after getting the response body
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError:
            return {}
