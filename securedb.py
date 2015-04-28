"""
A module for user authentication using SecureDB's authentication service.

SecureDB credentials are saved in a dictionary contained in credentials.py.
Please remember to secure credentials.py properly.
"""
import requests
import json

# Load SecureDB credentials from a separate file (credentials.py):
from credentials import credentials

# Store strings for forming API request URLs here:
base_url = 'http://api.securedb.co/securedbapi/account/'
authenticate_url = '/authenticate'

def authenticate(username, password):
  """Authenticate a user given the username and password.

  Returns the response from the authentication request. Since the
  authentication request is performed using Python Requests, the
  response format follows that of a response returned by
  requests.post(). See the following documentation for details:

  http://docs.python-requests.org/en/latest/user/quickstart/#response-content

  If securedb.co provided a response, response.content will contain JSON
  from SecureDB with information like a response string ("message") and, if
  authenticated, user ID ("data"). See the SecureDB documentation for the 
  Authenticate API call:

  https://api.securedb.co/swagger/index.html
  """
  # Form the URL by combining base url, cust id, dir id, and auth path:
  url = ( base_url +
          credentials['customer_id'] + '/' +
          credentials['directory_id'] +
          authenticate_url )

  # Specify application/json as the content type in the header:
  headers = {'Content-Type':'application/json'}

  # Provide the API key and Secret key as username, password for API authentication:
  auth = ( credentials['api_key'],
           credentials['secret_key'] ) 

  # Create the POST data containing the username and password passed to us:
  data = ( '{"userName": "' + username + '","password":"' + password + '"}' )

  # Make the request:
  return requests.post(url, data=data, auth=auth, headers=headers)


def is_authenticated(authenticate_response):
  """Determine user authentication from the response of the authenticate() function.

  This function returns True if authenticate_response indicates successful
  authentication, otherwise False is returned.
  """
  if (authenticate_response.status_code == 200):
    return True
  else:
    return False


def get_user_id(authenticate_response):
  """Get the user ID from the response of the authenticate() function.

  This function returns the user ID contained in the authenticate() function
  if the user was authenticated, otherwise it returns None.
  """
  if (is_authenticated(authenticate_response)):
    data = json.loads(authenticate_response.content)
    return data["data"]
  else:
    return None

