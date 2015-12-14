#!/bin/bash

# add /path/to/this/file at the end of /etc/bash.bashrc

if [[ -n $SSH_CONNECTION ]] && [[ -z $VIM ]] ; then
    /home/james/.login/push_login/push_login.py
fi


