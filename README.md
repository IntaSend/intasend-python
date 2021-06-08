# IntaSend Payments Gateway - Python SDK

## Setup and authenticating service

    from intasend import APIService

    private_key = """-----BEGIN PRIVATE KEY-----
        MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCwhxnB5aZD6EqF....8laHwYTQdDbAlCGZB992YoHl
        -----END PRIVATE KEY-----"""

    token = "YOUR-API-TOKEN"
    publishable_key = "YOUR-PUBLISHABLE-KEY"
    service = APIService(token="token",publishable_key=publishable_key, private_key=private_key)

## How to generate PRIVATE KEY

Use the following helper function to generate a RSA Key for nonce signing. Keep your private_key safe and share the public key with IntaSend. Note: These key pair is required only if you are sending money.


    from intasend.utils import generate_keys

    private_key, public_key = generate_keys()
    print(private_key)
    print(public_key)

## Services
    
    service = APIService(token="token",publishable_key=publishable_key, private_key=private_key)
    
    # Trigger M-Pesa STK Push
    response = service.collect.mpesa(phone_number=2547...,
                                      email="customer@example.com", amount=10, narrative="Fees")
    print(response)

    # Wallets Management
    response = service.wallets.retrieve()
    print(response)

    response = service.wallets.details(<WALLET-ID>)
    print(response)

    response = service.wallets.transactions(203)
    print(response)
    
    response = service.wallets.create("GBP")
    print(response)

    # Fund specific wallet
    response = service.wallets.fund(
         wallet_id=201, phone_number=25472.., email="customer@example.com", amount=10, narrative="Fees", name="Awesome Customer")
    print(response)

    # Wallet to wallet transfers
    response = service.wallets.intra_transfer(201, 328, 1, "Charge capture")
    print(response)

    # Retrieve Chargebacks
    response = service.chargebacks.retrieve(41)
    print(response)
    
    # Send money
    transactions = [{'name': 'Awesome Customer 1', 'account': 25472.., 'amount': 10},
                    {'name': 'Awesome Customer 2', 'account': 25472.., 'amount': 10000}]
    
    ## device_id - Note device id is the PSD2 device id from the dashboard - https://developers.intasend.com/apis/extra-payment-authentication
    response = service.transfer.mpesa(device_id=1, currency='KES', transactions=transactions)
    print(response)

    status = service.transfer.status(response.get("tracking_id"))
    print(f"Status: {status}")
