import os
import sys

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

# Sijax directory setup
SIJAX_STATIC_PATH = os.path.join(BASE_DIR, 'static/js/sijax/')
SIJAX_JSON_URI = '/static/js/sijax/json2.js'

# Define the upload directory
UPLOAD_DIR = os.path.realpath('network/files')

# Secret key for signing cookies
SECRET_KEY = b',chks\x9f|\x08\x94c-\x94\x90\xa5\xa2\xbd'
