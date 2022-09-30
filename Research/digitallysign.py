# Easy to use impl. of Elliptic Curve Dig. Signature Algorithm
# ecdsa can sign/verify the integrity of digital msgs.

from ecdsa import SigningKey

private_key = SigningKey.generate() # uses NIST192p
signature = private_key.sign(b"Educative authorizes this shot")
print(signature)
