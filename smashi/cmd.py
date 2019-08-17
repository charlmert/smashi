# adapted from https://git.styrion.net/iteas/iteas-tools/blob/master/proxmox/proxmox_install_PVE5.py

import sys
import subprocess
import pipes
import shlex
import pexpect

def run(command, argShell=False):
    return subprocess.call(shlex.split(command) if argShell == False else command, shell=argShell)

"""
answers in the form
[
    {
        'question': 'Expected Command Output Text',
        'answer': 'Answer to the question'
    },
    {
        'question': 'Password:',
        'answer': 'thepassword'
    },
]
"""
def expect(command, answers=None):
    child = pexpect.spawn(command)

    for answer in answers:
        child.expect(answer[0])
        child.sendline(answer[1])

    child.expect(pexpect.EOF, timeout=None)
    cmd_show_data = child.before
    cmd_output = cmd_show_data.split('\n')
    for data in cmd_output:
        print(data)

def output(command, answers=None, argShell=False):
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=argShell)
    ret = p.wait()
    return (ret, p.stdout.read().decode('UTF-8'), p.stderr.read().decode('UTF-8'))

def tail(command, argShell=False):
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=argShell)
    for c in iter(lambda: p.stdout.read(1), b''.decode('utf-8')):  # replace '' with b'' for Python 3
        sys.stdout.write(c.decode('utf-8'))

def stdout(command, argShell=False):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=argShell)
    ret = p.wait()
    return (ret, p.stdout.read().decode('UTF-8'))

def stderr(command, argShell=False):
    p = subprocess.Popen(command, stderr=subprocess.PIPE, shell=argShell)
    ret = p.wait()
    return (ret, p.stderr.read().decode('UTF-8'))

def stdin(command, argShell=False):
    p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=argShell)
    return p

def escapePayload(payload, enclosingQuote = '"'):
    if (enclosingQuote == '"'):
        return payload.replace('"', '\\"')
    if (enclosingQuote == '\''):
        return payload.replace('\'', '\\\'')
