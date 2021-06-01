from .client import APIBase


class Transfer(APIBase):
    def send_money(self, device_id, provider, currency, transactions, callback_url=None):
        payload = {
            "device_id": device_id,
            "provider": provider,
            "currency": currency,
            "transactions": transactions,
            "callback_url": callback_url
        }
        return self.send_request("POST", "send-money/initiate/", payload)

    def approve(self, account):
        pass

    def status(self, account):
        pass

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
