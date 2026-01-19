from growwapi import GrowwAPI
import pyotp
 
api_key = "YOUR_TOTP_TOKEN"
 
# totp can be obtained using the authenticator app or can be generated like this
totp_gen = pyotp.TOTP('YOUR_TOTP_SECRET')
totp = totp_gen.now()
 
access_token = GrowwAPI.get_access_token(api_key=api_key, totp=totp)
# Use access_token to initiate GrowwAPI
groww = GrowwAPI(access_token)