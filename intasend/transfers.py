from .client import APIBase


class Transfer(APIBase):
    def mpesa(self, phone_number, email, amount, narrative, currency="KES", api_ref="API Request", name=None):
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
        return self.send_request("payment/collection/", payload)

    def intasend(self, phone_number, email, amount, narrative, currency="KES", api_ref="API Request", name=None):
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
        return self.send_request("payment/collection/", payload)

    # def bank(self, phone_number, email, amount, narrative, currency="KES", api_ref="API Request", name=None):
    #     payload = {
    #         "public_key": self.publishable_key,
    #         "currency": currency,
    #         "method": "M-PESA",
    #         "amount": amount,
    #         "phone_number": phone_number,
    #         "api_ref": api_ref,
    #         "name": name,
    #         "email": email
    #     }
    #     return self.send_request("payment/collection/", payload)
