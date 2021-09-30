    
import time
from typing import Dict

import jwt
from decouple import config

# Constants holding the secret string and the algorithm being used to sign JWT tokens
# Both of these will be coming from .env 
JWT_SECRET = 'deff1952d59f883ece2hgh867897dhjkghf60e8683fed21ab0ad9a53323eca4f'
JWT_ALGORITHM = 'HS256'


# A helper function which takes token as argument and returns the response as dict
def token_response(token: str):
    return {"access_token": token, }


# Function to sign (encode) the JWT token, it takes the user_id 
# as argument for whom the token is being created
def signJWT(user_id: int) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


# A helper function to return response while decoding JWT token in decodeJWT function
def generate_response(success: bool, token: str, error:str):
    return {'success':success, 'token':token, 'error':error}

# Function to decode the specified JWT token, if the token is successfully decoded 
# and it is not expired as well then the decoded token will be returned
def decodeJWT(token: str) -> dict:
   
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return generate_response(True, decoded_token, None) if decoded_token["expires"] >= time.time() else generate_response(False, None, 'Token Expired')
    except:
        return generate_response(False, None, 'Unable to verify user token')