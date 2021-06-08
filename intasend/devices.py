from .client import APIBase


class Devices(APIBase):
    def details(self, device_id):
        return self.send_request("GET", f"r'account-devices'/{device_id}", None)

    def retrieve(self, device_id=None):
        if device_id:
            return self.details(device_id)
        return self.send_request("GET", "r'account-devices'/", None)
