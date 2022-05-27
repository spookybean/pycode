import pyotp


totp = pyotp.TOTP('WH5X4NKE4JUPWUVFRMM4E3KEOHTO6KWD', interval=5)

otp = totp.now()
print(otp)