"""A Flask server demonstrating authentication using SecureDB.

This code demonstrates a call to the securedb.authenticate() function
in securedb.py. See this call in the do_login() function, below.

The Flask server is an HTTPS server. HTTPS is used so that the
username and password are not posted to this server in plaintext.
No attempt has been made to determine whether or not this use of
HTTPS is actually secure.

Requires Python 2.7.9 for TLS features for the HTTPS server. Python 
packages and Ubuntu versions:

Ubuntu Version  Python Version
--------------  --------------
14.04 LTS       2.7.6
14.10           2.7.8
15.04           2.7.9
"""

from flask import Flask, request, render_template

# This module (in securedb.py) contains helpers for performing 
# user authentication using SecureDB:
import securedb

# The HTTPS code comes from http://flask.pocoo.org/snippets/111/
# For instructions on creating cert.pem and key.pem, which must
# in the same directory as this file, please refer to
# http://stackoverflow.com/questions/10175812/how-to-create-a-self-signed-certificate-with-openssl
# Finally, refer to the Python ssl module documentation at
# https://docs.python.org/2/library/ssl.html
# for important information about security considerations of using SSL.
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')

app = Flask(__name__)

# Flask server configuration parameters go here:
host =  '0.0.0.0'	# listen on any address
port =  8000            # listen on port 8000
debug = True            # enable debug output

@app.route('/')
def login_form():
  """Provides a form for entering a username and password for authentication."""
  return render_template('login.html')


@app.route('/login', methods = ['POST'])
def do_login():
  """Authenticates a POSTed username and password."""
  # Use SecureDB to authenticate user. See the authenticate() method
  # in securedb.py for more information.
  response = securedb.authenticate(request.form['username'], 
                                   request.form['password'])

  # Proceed based on response:
  if (securedb.is_authenticated(response)):
    return render_template( 'login_success.html',
                            user_id=securedb.get_user_id(response),
                            status_code=response.status_code,
                            content=response.content )
  else:
    return render_template( 'login_fail.html',
                            status_code=response.status_code, 
                            content=response.content )


# Start the Flask server:
if __name__ == '__main__':
  app.run(host=host, port=port, debug=debug, ssl_context=context)
