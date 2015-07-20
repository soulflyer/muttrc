#!/usr/bin/python
import re, subprocess
def get_keychain_pass(label=None):
    params = {
        'security': '/usr/bin/security',
        'command': 'find-generic-password',
        'label': label,
        'keychain': '/Users/iain/Library/Keychains/login.keychain',
    }
    command = "sudo -u iain %(security)s -v %(command)s -g -l %(label)s %(keychain)s" % params
    print "hello from python"
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    outtext = [l for l in output.splitlines()
               if l.startswith('password: ')][0]

    return re.match(r'password: "(.*)"', outtext).group(1)
