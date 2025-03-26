from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()

blacklisted_tokens = set()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    """
        This function is called before any protected endpoint is accessed.
        It checks if the token (jti) is in the blacklist.
    """
    jti = jwt_payload.get("jti")
    print(f"Checking if token is revoked: {jti} in {blacklisted_tokens}")
    return jti in blacklisted_tokens