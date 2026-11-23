from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
import jwt 
from app.core.config import settings

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)      # Generating a random salt.Applying Argon2id.Using the configured parameters.Producing the encoded hash.

def verify_password(plain_password: str, hashed_password:str) -> bool: 
    return password_hash.verify(plain_password, hashed_password)
#user enumeration

def create_access_token(data: dict, expires_delta : timedelta | None = None) -> str:
    to_encode = data.copy()  #copying the data dictionary so that we are identifying only the copy part by adding the additional JWT information and not the original one 
    if expires_delta : 
        expire = datetime.now(timezone.utc) + expires_delta
    else: 
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": datetime.now(timezone.utc)})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY,  algorithm=settings.ALGORITHM)      #This is where the actual token is generated.- to_encode: Payload. - SECRET_KEY: Secret used to sign the token. - algorithm: Signing algorithm, currently HS256. The returned value is a signed JWT string.

    return encoded_jwt
    #Now the generated token can be returned to the client.

def decode_access_token(token: str) -> dict:
    try: 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM], options={"require": ['exp', 'sub']})
        #PyJWT performs Signature , expiration, algorithm verification and required claims 
        #options Ensures that the token contains the required claims.
        return payload
    except jwt.InvalidTokenError as error:
        raise ValueError("Invalid or expired Token0") from error 