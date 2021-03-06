import os
import sys

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

# Define the upload directory
UPLOAD_DIR = os.path.realpath('netdrive/drive')

# Secret key for signing cookies
SECRET_KEY = b',chks\x9f|\x08\x94c-\x94\x90\xa5\xa2\xbd'

# Blocked extensions by default
BLOCKED_EXT = ['.exe', '.bat', '.dll', '.sfx', '.tmp']
