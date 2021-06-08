from .client import APIBase
from .collections import Collect


class Wallet(APIBase):
    def __init__(self, **kwargs):
        """Wallets management service."""
        self.collect = Collect(**kwargs)
        super().__init__(**kwargs)

    def details(self, wallet_id):
        return self.send_request("GET", f"wallets/{wallet_id}", None)

    def create(self, currency):
        payload = {
            "wallet_type": "WORKING",
            "currency": currency
        }
        return self.send_request("POST", "wallets/", payload)

    def retrieve(self, wallet_id=None):
        if wallet_id:
            return self.details(wallet_id)
        return self.send_request("GET", "wallets/", None)

    def transactions(self, wallet_id):
        return self.send_request("GET", f"wallets/{wallet_id}/transactions", None)

    def intra_transfer(self, origin_id, destination_id, amount, narrative):
        payload = {
            "wallet_id": destination_id,
            "amount": amount,
            "narrative": narrative
        }
        return self.send_request("POST", f"wallets/{origin_id}/intra_transfer/", payload=payload)

    def fund(self, wallet_id, phone_number, email, amount, narrative, currency="KES", api_ref="API Request", name=None):
        return self.collect.mpesa(phone_number=phone_number, email=email, amount=amount, narrative=narrative, currency=currency, api_ref=api_ref, name=name)
