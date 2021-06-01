from .client import APIBase
import OpenSSL
from OpenSSL import crypto as OpenSSLCrypto
import base64


class Transfer(APIBase):
    def _sign_message(self, private_key, message):
        pkey = OpenSSLCrypto.load_privatekey(
            OpenSSLCrypto.FILETYPE_PEM, private_key, None)
        sign = OpenSSL.crypto.sign(pkey, message, "sha256")
        return sign.hex()

    def send_money(self, device_id, provider, currency, transactions, callback_url=None):
        payload = {
            "device_id": device_id,
            "provider": provider,
            "currency": currency,
            "transactions": transactions,
            "callback_url": callback_url
        }
        return self.send_request("POST", "send-money/initiate/", payload)

    def approve(self, payload):
        nonce = payload["nonce"]
        signed_nonce = self._sign_message(
            self.private_key.encode("utf-8"), nonce)
        payload["nonce"] = signed_nonce
        return self.send_request("POST", "send-money/approve/", payload)

    def status(self, tracking_id):
        payload = {
            "tracking_id": tracking_id
        }
        return self.send_request("POST", "send-money/status/", payload)

    def mpesa(self,  device_id, currency, transactions, callback_url=None):
        provider = "MPESA-B2C"
        return self.send_money(device_id, provider, currency, transactions, callback_url)

    def mpesa_b2b(self,  device_id, currency, transactions, callback_url=None):
        provider = "MPESA-B2B"
        return self.send_money(device_id, provider, currency, transactions, callback_url)

    def intasend(self, device_id, currency, transactions, callback_url=None):
        provider = "INTASEND"
        return self.send_money(device_id, provider, currency, transactions, callback_url)

    def bank(self, device_id, currency, transactions, callback_url=None):
        provider = "PESALINK"
        return self.send_money(device_id, provider, currency, transactions, callback_url)
