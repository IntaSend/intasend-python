from .client import APIBase
from .utils import sign_message


class Transfer(APIBase):
    def send_money(self, device_id, provider, currency, transactions, callback_url=None, wallet_id=None):
        payload = {
            "device_id": device_id,
            "provider": provider,
            "currency": currency,
            "transactions": transactions,
            "callback_url": callback_url,
            "wallet_id": wallet_id
        }
        return self.send_request("POST", "send-money/initiate/", payload)

    def approve(self, payload):
        nonce = payload["nonce"]
        signed_nonce = sign_message(self.private_key.encode("utf-8"), nonce)
        payload["nonce"] = signed_nonce
        return self.send_request("POST", "send-money/approve/", payload)

    def status(self, tracking_id):
        payload = {
            "tracking_id": tracking_id
        }
        return self.send_request("POST", "send-money/status/", payload)

    def mpesa(self,  device_id, currency, transactions, callback_url=None, wallet_id=None):
        provider = "MPESA-B2C"
        return self.send_money(device_id, provider, currency, transactions, callback_url, wallet_id)

    def mpesa_b2b(self,  device_id, currency, transactions, callback_url=None, wallet_id=None):
        provider = "MPESA-B2B"
        return self.send_money(device_id, provider, currency, transactions, callback_url, wallet_id)

    def intasend(self, device_id, currency, transactions, callback_url=None, wallet_id=None):
        provider = "INTASEND"
        return self.send_money(device_id, provider, currency, transactions, callback_url, wallet_id)

    def bank(self, device_id, currency, transactions, callback_url=None, wallet_id=None):
        provider = "PESALINK"
        return self.send_money(device_id, provider, currency, transactions, callback_url, wallet_id)
