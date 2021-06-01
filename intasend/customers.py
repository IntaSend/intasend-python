from .client import APIBase


class Customers(APIBase):
    def details(self, id):
        return self.send_request("GET", f"customers/{id}", None)

    def create(self, currency):
        payload = {
            # "wallet_type": "WORKING",
            # "currency": currency
        }
        return self.send_request("POST", "customers/", payload)

    def retrieve(self, id=None):
        if id:
            return self.details(id)
        return self.send_request("GET", "customers/", None)

    def transactions(self, id):
        return self.send_request("GET", f"customers/{id}/transactions", None)
