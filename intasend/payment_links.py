from .client import APIBase


class PaymentLinks(APIBase):
    def details(self, id):
        return self.send_request("GET", f"r'account-devices'/{id}", None)

    def create(self, currency):
        payload = {
            # "wallet_type": "WORKING",
            # "currency": currency
        }
        return self.send_request("POST", "r'account-devices'/", payload)

    def retrieve(self, id=None):
        if id:
            return self.details(id)
        return self.send_request("GET", "r'account-devices'/", None)

    def deactivate(self):
        return self.send_request("GET", "r'account-devices'/", None)

    def update(self):
        return self.send_request("GET", "r'account-devices'/", None)
