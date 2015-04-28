"""
Copyright 2015 PhoneDeveloper LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

#
# Copy this file to config.py, set permissions to execute-only, and then replace the values below.
#
# See https://securedb.co/quick_start.html if you need help finding these values.
#
# - customer_id is your SecureDB customer id
# - directory_id is the directory id where your users are located in SecureDB
# - api_key is the 'API Key' from credentials.csv
# - secret_key is the 'Secret Key' from credentials.csv
# - basic_auth is the 'BA Header Value' from credentials.csv, NOT INCLUDING
#   'Authorization: ' at the beginning of the value.
#
# Be sure not to add config.py with your filled-in values to a repository!
#

credentials = {
  'customer_id':      'your SecureDB customer id',
  'directory_id':     'your SecureDB directory',
  'api_key':          'the API Key from credentials.csv',
  'secret_key':       'the Secret Key from credentials.csv',
  'basic_auth':       'the BA Header Value from credentials.csv'
}
