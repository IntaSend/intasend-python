from .client import APIBase

class Transfer(APIBase):
    def send_money(self, provider, currency, transactions, callback_url=None, wallet_id=None):
        payload = {
            "provider": provider,
            "currency": currency,
            "transactions": transactions,
            "callback_url": callback_url,
            "wallet_id": wallet_id
        }
        return self.send_request("POST", "send-money/initiate/", payload)

    def approve(self, payload):
        return self.send_request("POST", "send-money/approve/", payload)

    def status(self, tracking_id):
        payload = {
            "tracking_id": tracking_id
        }
        return self.send_request("POST", "send-money/status/", payload)

    def mpesa(self, currency, transactions, callback_url=None, wallet_id=None):
        provider = "MPESA-B2C"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id)

    def mpesa_b2b(self, currency, transactions, callback_url=None, wallet_id=None):
        provider = "MPESA-B2B"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id)

    def intasend(self, currency, transactions, callback_url=None, wallet_id=None):
        provider = "INTASEND"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id)

    def bank(self, currency, transactions, callback_url=None, wallet_id=None):
        provider = "PESALINK"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id)
    
    def get_bank_codes(self):
        return self.send_request("GET", "send-money/bank-codes/ke/", {}, noauth=True)
    
    def airtime(self, currency="KES", transactions=[], callback_url=None, wallet_id=None):
        provider = "AIRTIME"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id)
