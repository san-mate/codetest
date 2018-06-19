#!/bin/python

import re

if __name__ == '__main__':
    passwords = raw_input()
    for password in passwords.split(','):
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[*#+@])[A-Za-z0-9*#+@]{4,6}$', password):
            print password
