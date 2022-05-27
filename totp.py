import pyotp
import time

totp = pyotp.TOTP('WH5X4NKE4JUPWUVFRMM4E3KEOHTO6KWD', interval=5)

otp = totp.now()
print(otp)

print(totp.verify(totp.now()))
time.sleep(5)
print(totp.verify(totp.now()))