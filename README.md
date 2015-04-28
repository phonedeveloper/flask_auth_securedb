# SecureDB authentication example for Flask

This project shows how to authenticate a user in SecureDB, which is a service that provides encrypted user management (securedb.co).

## Motivation

SecureDB was a sponsor at a recent hackathon. Our team won hover drones for implementing user authentication using SecureDB. Since setting up and managing a secure user database is a lot of work for my rapid prototyping projects, I'd like to use these guys in the future and wanted to document this. The REST API is pretty easy as long as you get the header correct (which this example does.) And, the hover drone is cool - thanks guys!

## How it works

Pretty much all you need to know if found in <code>securedb.py</code>. This is a module that provides a function that performs the authentication.

<code>flask_securedb.py</code> is a Flask server that calls this authentication function to authenticate a user.

Authentication is done within the <code>authenticate()</code> method in <code>securedb.py</code> by POSTing the username and password to a REST API at securedb.co, and getting the JSON response.

If authentication is successful, a user ID will be returned by securedb which can be used as your user identifier for session management in Flask.

A couple of other simple helper functions are provided in <code>securedb.py</code> that will return the user ID or whether or not authentication was successful if you pass them the output of the <code>authenticate()</code> call.

This sample only shows the authentication part, not session management. Flask-login, documented at https://flask-login.readthedocs.org/en/latest/, is one possible candidate for session management.

## Examples

The login screen, provided by the Flask server at https://localhost:8000. This is provided only to give you an easy way to enter a username and password that will be supplied to the authentication function.

![Login form](/doc/login.png)

### Sample Responses

The responses in the screenshots below which are labeled <code>Response code</code> and <code>Response message</code> are found in the response object's <code>response.status_code</code> and <code>response.content</code> fields, respectively.

Below is an example of a successful authentication. Note the user ID returned as the value for the <code>"data"</code> key:

![Successful authentication](/doc/success.png)

A sample response, where the username was not recognized:

![Invalid username](/doc/invalid_username.png)

A sample response, where the password was not recognized:

![Invalid password](/doc/invalid_password.png)



## Files

These are the files of interest:

* <code>securedb.py</code> - a small module which provides an <code>authenticate</code> function, which is a wrapper around an HTTPS POST to the SecureDB authentication REST API.
* <code>credentials_template.py</code> - cppy to <code>credentials.py</code> and plug in your SecureDB credentials (see Setup, below).
* <code>flask_securedb.py</code> - a small Flask app that demonstrates authentication. It calls securedb.authenticate() from within its do_login() function.
* <code>templates</code> folder - HTML templates for Flask
* <code>static</code> folder - contains a smiple stylesheet for the Flask pages.

## Setup

First, you must copy <code>credentials_template.py</code> to <code>credentials.py</code> and fill in your SecureDB credentials as described in <code>credentials_template.py</code>.

Second, for the Flask HTTPS server to work, you'll need to generate a private key file <code>key.pem</code> and certificate <code>cert.pem</code> and place them in the same folder as <code>flask_securedb.py</code>. A link to a StackOverflow question on how to do this is provided in <code>flask_securedb.py</code>

IMPORTANT: Be sure to set the permissions for <code>credentials.py</code>, <code>key.pem</code> and <code>cert.pem</code> so that they are not accessible by other users on your system.

Third, run the Flask server using <code>$ python flask_securedb.py</code>. This is best done in a virtual environment (see below.) Point a browser on the same machine to https://localhost:8000 to get a login form in which you can enter a username and password. Since your server is using a self-signed certificate, you will need to override your browser's security warning.


A few things to keep in mind:
* Python 2.7.9 is needed to support TLS for the Flask HTTPS server. Earlier versions of Python can be made to work, although less securely. See the link for the Flask HTTPS documentation inside <code>flask_securedb.py</code>. Python 2.7.9 doesn't appear in Ubuntu releases until Ubuntu version 15.04.
* Consider running this in a virtual environment:
  * Install the virtual environment, In the project root, run <code>$ virtualenv venv</code>. Activate the virtual enviroment using the command <code>$ . venv/bin/activate</code>. Use <code>pip</code> to install Flask, requests, and anything else Python barks about when you try to run the server.
* You'll only be able to test authentication failure until you set up a user. How to do this manually is described in securedb's 10 minute Quick Start found at https://securedb.co/quick_start.html.

## License

Please see <code>LICENSE</code> for license information. <code>securedb.py</code> and <code>credentials_template.py</code> use a BSD license and all others use the Flask BSD license. This is described in <code>LICENSE</code>.
