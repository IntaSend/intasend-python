from .client import APIBase


class Chagebacks(APIBase):
    def create(self, invoice, amount, reason, reason_details=None):
        payload = {
            "invoice": invoice,
            "amount": amount,
            "reason": reason,
            "reason_details": reason_details
        }
        return self.send_request("POST", "chargebacks/", payload)

    def retrieve(self, id=None):
        if id:
            return self.details(id)
        return self.send_request("GET", "chargebacks/", {})

    def details(self, id=None):
        return self.send_request("GET", f"chargebacks/{id}/", {})
