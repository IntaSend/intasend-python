import requests


class APIBase(object):
    def __init__(self, **kwargs):
        self.token = kwargs.get("token")
        self.publishable_key = kwargs.get("publishable_key")
        if not self.token:
            raise Exception("Authentication token is required")
        super().__init__()

    def send_request(self, request_type, service_endpoint, payload):
        url = self.get_service_url(service_endpoint)
        headers = self.get_headers()
        resp = requests.request(
            request_type, url, json=payload, headers=headers)
        if resp.status_code != 200:
            print(url)
            raise Exception(resp.text)
        return resp.json()

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}"
        }

    def get_service_url(self, service_endpoint):
        return f"https://sandbox.intasend.com/api/v1/{service_endpoint}"
