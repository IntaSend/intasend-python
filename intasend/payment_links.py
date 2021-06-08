from .client import APIBase


class PaymentLinks(APIBase):
    def details(self, link_id):
        return self.send_request("GET", f"payment-links'/{link_id}", None)

    def create(self, name, amount, currency, **kwargs):
        payload = kwargs
        payload["name"] = name
        payload["currency"] = currency
        payload["amount"] = amount
        return self.send_request("POST", "payment-links'/", payload)

    def retrieve(self, link_id=None):
        if link_id:
            return self.details(link_id)
        return self.send_request("GET", "payment-links'/", None)

    def deactivate(self):
        return self.send_request("GET", "payment-links'/", None)

    def update(self):
        return self.send_request("GET", "payment-links'/", None)
