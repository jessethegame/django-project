#!/usr/bin/env python

import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
NAME = os.path.split(ROOT)[1]

def try_mkdir(path):
    try:
        os.makedirs(path)
    except OSError:
        pass

def main():
    try:
        LOCAL = sys.argv[1]
    except IndexError:
        LOCAL = os.path.join(ROOT, 'local')

    print 'cd %s' % ROOT
    os.chdir(ROOT)
    print 'mkdir local'
    try_mkdir(LOCAL)
    print 'cd local'
    os.chdir(LOCAL)
    print 'mkdir log'
    try_mkdir('log')
    print 'mkdir -p cache/egg'
    try_mkdir('cache/egg')
    print 'mkdir shared'
    try_mkdir('shared')
    print 'mkdir celery'
    try_mkdir('celery')

    # Create the virtualenv with virtualenvwrapper
    ENV = os.path.join(LOCAL, 'venv')

    print 'virtualenv', ENV
    subprocess.call(['virtualenv', ENV])

    activate = os.path.join(ENV, 'bin', 'activate')
    print activate
    subprocess.call([activate])

    print 'cd ..'
    os.chdir(ROOT)

    print 'pip install -r requirements.pip'
    subprocess.call(['pip', 'install', '-r', os.path.join(ROOT.encode(), 'requirements.pip')])


if __name__ == '__main__':
    main()
