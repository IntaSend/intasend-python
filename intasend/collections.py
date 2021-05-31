from .client import APIBase


class Collect(APIBase):
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
        return self.send_request("POST", "payment/collection/", payload)

    def get_quote(self, amount, method, currency="KES", mobile_tarrif="BUSINESS-PAYS", card_tarrif="BUSINESS-PAYS"):
        payload = {
            "public_key": self.publishable_key,
            "currency": currency,
            "method": method,
            "mobile_tarrif": mobile_tarrif,
            "card_tarrif": card_tarrif
        }
        return self.send_request("POST", "payment/collection/", payload)
