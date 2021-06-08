from Crypto.PublicKey import RSA
import OpenSSL
from OpenSSL import crypto as OpenSSLCrypto


def generate_keys():
    """
    Returns a private and public key.

    Returns:
        tupple: values of generated private and public key
    """
    key = RSA.generate(2048)
    private_key = key.export_key('PEM')
    public_key = key.publickey().export_key('PEM')
    return private_key, public_key


def sign_message(private_key, message):
    """
    Sign message with the private key.

    Args:
        private_key (byte): Private key
        message (string): Message to sign

    Returns:
        string: Signed message
    """
    pkey = OpenSSLCrypto.load_privatekey(
        OpenSSLCrypto.FILETYPE_PEM, private_key, None)
    sign = OpenSSL.crypto.sign(pkey, message, "sha256")
    return sign.hex()
