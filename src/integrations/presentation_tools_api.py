```python
import requests

class PresentationToolsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.presentationtools.com"

    def generate_presentation(self, presentation_content, presentation_structure):
        url = f"{self.base_url}/generate"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "content": presentation_content,
            "structure": presentation_structure
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to generate presentation: {response.text}")

    def get_presentation(self, presentation_id):
        url = f"{self.base_url}/presentations/{presentation_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get presentation: {response.text}")
```