#used for creating tokens 
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
# used for storing tokens in the database.
from rest_framework.authtoken.models import Token

class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'