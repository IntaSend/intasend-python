# IntaSend Payment Gateway - Python SDK

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3441c7d731e64e899b8ca3f125422f9a)](https://app.codacy.com/gh/IntaSend/intasend-python?utm_source=github.com&utm_medium=referral&utm_content=IntaSend/intasend-python&utm_campaign=Badge_Grade_Settings)

## Official documentation

Python SDK for [IntaSend Payment Gateway](https://intasend.com). IntaSend enables you to easily add payments to your application with a few lines of code.

Follow the instruction below to install and get started.

Visit our [sandbox/developers](https://sandbox.intasend.com) test for your API Keys.

Checkout our [API documentation](https://developers.intasend.com/) for more details and for payload references.

## How to install

    pip install intasend-python

## Authenticating service

    from intasend import APIService

    token = "YOUR-API-TOKEN"
    publishable_key = "YOUR-PUBLISHABLE-KEY"
    service = APIService(token="token",publishable_key=publishable_key)

## Examples

    # Remember to switch of test when going live by removing the flag or set it to False

    service = APIService(token="token",publishable_key=publishable_key, test=True)
    
    # Collect payments
    ## Generate checkout URL
    response = service.collect.checkout(phone_number=2547...,
                                        email="felix@intasend.com", amount=10, currency="KES", comment="Fees")
    print(response)

    ## Get payment status using invoice/tracking id
    response = service.collect.status(invoice_id="NR5XKGY")
    print(response)

    ## Trigger M-Pesa STK Push
    response = service.collect.mpesa_stk_push(phone_number=2547...,
                                      email="customer@example.com", amount=10, narrative="Fees")
    print(response)

    # Wallets Management
    response = service.wallets.retrieve()
    print(response)

    response = service.wallets.details(<WALLET-ID>)
    print(response)

    response = service.wallets.transactions(<WALLET-ID>)
    print(response)
    
    response = service.wallets.create(currency="KES", label="API-WALLET", can_disburse=True)
    print(response)

    # Fund specific wallet
    response = service.wallets.fund(
         wallet_id=<WALLET-ID>, phone_number=25472.., email="customer@example.com", amount=10, narrative="Fees", name="Awesome Customer")
    print(response)

    # Wallet to wallet transfers
    response = service.wallets.intra_transfer(<WALLET-ID-1>, <WALLET-ID-2>, 1, "Charge capture")
    print(response)

    # Retrieve Chargebacks
    response = service.chargebacks.retrieve(<CHARGEBACK-ID>)
    print(response)
    
    # Send money
    transactions = [{'name': 'Awesome Customer 1', 'account': 25472.., 'amount': 10},
                    {'name': 'Awesome Customer 2', 'account': 25472.., 'amount': 10000}]
                    
    response = service.transfer.mpesa(currency='KES', transactions=transactions)
    print(response)

    status = service.transfer.status(response.get("tracking_id"))
    print(f"Status: {status}")

    # Buy AIRTIME
    transactions = [{'name': 'Joe Doe' ,'account': '25472...'}]
    response = service.transfer.airtime(currency='KES', transactions=transactions)
    print(response)
