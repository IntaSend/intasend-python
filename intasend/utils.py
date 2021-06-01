from Crypto.PublicKey import RSA


def generate_keys():
    """
    Returns a private and public key
    """
    key = RSA.generate(2048)
    private_key = key.export_key('PEM')
    public_key = key.publickey().export_key('PEM')
    return private_key, public_key
