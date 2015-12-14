#!/usr/bin/python

import os
from subprocess import call

if os.environ.get('SSH_CONNECTION') and not os.environ.get('VIM'):
    location = os.path.dirname(os.path.realpath(__file__))
    call(['{}/push_login/push_login.py'.format(location)])

