from .client import APIBase
from .collections import Collect
from .transfers import Transfer
from .wallets import Wallet


class APIService:
    def __init__(self, **kwargs):
        self.collect = Collect(**kwargs)
        self.transfer = Transfer(**kwargs)
        self.wallets = Wallet(**kwargs)
