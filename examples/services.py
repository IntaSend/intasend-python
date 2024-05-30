import secrets
import os
from intasend import APIService

TEST_PHONE_NUMBER = os.environ.get("TEST_PHONE_NUMBER")
TEST_API_TOKEN = os.environ.get("TEST_API_TOKEN")
TEST_PUBLISHABLE_KEY = os.environ.get("TEST_PUBLISHABLE_KEY")

service = APIService(token=TEST_API_TOKEN,
                     publishable_key=TEST_PUBLISHABLE_KEY, test=True)

if __name__ == "__main__":
    print("Running service")
    title = f"Link - {secrets.randbelow(20000)}"
    response = service.payment_links.create(
        title=title, currency="KES", amount=10)
    print(response)
    response = service.collect.mpesa_stk_push(phone_number=TEST_PHONE_NUMBER,
                                              email="tests@example.com", amount=10, narrative="Fees")
    print(response)

    response = service.wallets.retrieve()
    print(response)

    response = service.wallets.details("ZQMMOQO")
    print(response)

    response = service.wallets.transactions("ZQMMOQO")
    print(response)
    response = service.wallets.create(
        currency="KES", label="API-WALLET", can_disburse=True)
    print(response)

    response = service.wallets.fund(
        wallet_id="ZQMMOQO", phone_number=TEST_PHONE_NUMBER, email="tests@example.com", amount=10, narrative="Fees", name="FELIX C")
    print(response)

    response = service.wallets.intra_transfer(
        "ZQMMOQO", "XZY43Q8", 1, "Charge capture")
    print(response)

    response = service.chargebacks.retrieve("EYVBZR2")
    print(response)
    transactions = [{'name': 'test-name', 'account': TEST_PHONE_NUMBER, 'amount': 10},
                    {'name': 'test-name', 'account': TEST_PHONE_NUMBER, 'amount': 10000}]
    requires_approval = 'YES' # Set to 'NO' if you want the transaction to go through without calling the approve method
    response = service.transfer.mpesa(currency='KES', transactions=transactions, requires_approval=requires_approval)
    print(response)

    if requires_approval == 'YES':
        response = service.transfer.approve(response)
        print(f"Approve response: {response}")
    
    status = service.transfer.status(response.get("tracking_id"))
    print(f"Status: {status}")

    response = service.collect.checkout(phone_number=TEST_PHONE_NUMBER,
                                        email="tests@example.com", amount=10, currency="KES", comment="Fees")
    print(response)

    response = service.collect.status(invoice_id="NR5XKGY")
    print(response)
