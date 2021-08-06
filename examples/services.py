import secrets
import os
from intasend import APIService
# from intasend.utils import generate_keys

TEST_PRIVATE_KEY = os.environ.get("TEST_PRIVATE_KEY")
TEST_PHONE_NUMBER = os.environ.get("TEST_PHONE_NUMBER")
TEST_API_TOKEN = os.environ.get("TEST_API_TOKEN")
TEST_PUBLISHABLE_KEY = os.environ.get("TEST_PUBLISHABLE_KEY")

service = APIService(token=TEST_API_TOKEN,
                     publishable_key=TEST_PUBLISHABLE_KEY, private_key=TEST_PRIVATE_KEY, test=True)

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
    response = service.wallets.create("EUR")
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
    response = service.transfer.mpesa(
        device_id="KZQMORO", currency='KES', transactions=transactions)
    print(response)

    status = service.transfer.status(response.get("tracking_id"))
    print(f"Status: {status}")

    response = service.transfer.approve(response)
    print(f"Approve response: {response}")
    # private_key, public_key = generate_keys()
    # print(private_key)
    # print("x"*10)
    # print(public_key)

    response = service.collect.checkout(phone_number=TEST_PHONE_NUMBER,
                                        email="tests@example.com", amount=10, currency="KES", comment="Fees")
    print(response)

    response = service.collect.status(invoice_id="NR5XKGY")
    print(response)
