from __future__ import annotations
from typing import Dict, Iterable

from intasend.exceptions import NarrativeExceedsLengthLimit
from .client import APIBase

class Transfer(APIBase):
    def send_money(self, provider, currency, transactions, callback_url=None, wallet_id=None, requires_approval='YES'):
        if not transactions:
            raise ValueError("Transaction details required")
      
        payload = {
            "provider": provider,
            "currency": currency,
            "transactions": transactions,
            "requires_approval":requires_approval,
            "callback_url": callback_url,
            "wallet_id": wallet_id
        }
        _ = _validate_transaction_data(transactions)
        return self.send_request("POST", "send-money/initiate/", payload)

    def approve(self, payload):
        return self.send_request("POST", "send-money/approve/", payload)

    def status(self, tracking_id):
        payload = {
            "tracking_id": tracking_id
        }
        return self.send_request("POST", "send-money/status/", payload)

    def mpesa(self, currency, transactions, requires_approval="YES", callback_url=None, wallet_id=None):
        provider = "MPESA-B2C"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id, requires_approval)

    def mpesa_b2b(self, currency, transactions, requires_approval="YES",callback_url=None, wallet_id=None):
        provider = "MPESA-B2B"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id, requires_approval)

    def intasend(self, currency, transactions, requires_approval="YES",callback_url=None, wallet_id=None):
        provider = "INTASEND"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id, requires_approval)

    def bank(self, currency, transactions, requires_approval="YES",callback_url=None, wallet_id=None):
        provider = "PESALINK"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id, requires_approval)
    
    def get_bank_codes(self):
        return self.send_request("GET", "send-money/bank-codes/ke/", {}, noauth=True)
    
    def airtime(self, currency="KES", transactions=None, requires_approval="YES", callback_url=None, wallet_id=None):
        provider = "AIRTIME"
        return self.send_money(provider, currency, transactions, callback_url, wallet_id, requires_approval)


def _validate_transaction_data(transactions: Iterable[Dict[str, str]]) -> None:
    for transaction in transactions:
        if transaction['narrative']:
            if len(transaction['narrative']) > 22:
                errmsg = "String values beyond 22 chars are truncated by default."
                raise NarrativeExceedsLengthLimit(errmsg)
