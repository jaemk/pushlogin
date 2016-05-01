#!/usr/bin/python3

import os
from subprocess import call

import settings


def login_event():
    return os.environ.get('SSH_CONNECTION') and\
           not os.environ.get('VIM') and\
           not os.environ.get('STY')


def main():
    if login_event():
        location = os.path.dirname(os.path.realpath(__file__))
        
        python_venv = settings.virtualenv_name
        python_exec = '{}/{}/bin/python'.format(location, python_venv)
        pushlogin_file = '{}/pushlogin.py'.format(location)
        
        call([python_exec, pushlogin_file])


if __name__ == '__main__':
    main()
