from .client import APIBase


class Wallet(APIBase):
    def details(self, id):
        return self.send_request("GET", f"wallets/{id}", None)

    def create(self, phone_number, email, amount, narrative, currency="KES", api_ref="API Request", name=None):
        payload = {
            "public_key": self.publishable_key,
            "currency": currency,
            "method": "M-PESA",
            "amount": amount,
            "phone_number": phone_number,
            "api_ref": api_ref,
            "name": name,
            "email": email
        }
        return self.send_request("POST", "wallets/", payload)

    def list(self):
        return self.send_request("GET", "wallets/", None)

    def transactions(self, id):
        return self.send_request("GET", f"wallets/{id}/transactions", None)

    def intra_transfer(self, origin_id, destination_id, amount, narrative):
        pass
