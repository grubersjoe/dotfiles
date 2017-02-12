#!/usr/bin/env python3

import i3ipc
from json import load
from socket import gethostname
from shutil import copyfileobj

CONF_FILE = './config'

with open(CONF_FILE, 'w') as config:
    try:
        # load the theme
        with open('../theme/theme.json') as t:
            theme = load(t)
        # and append the variables to i3 config
        config.write('# THEME\n')
        for name, hexcode in theme.items():
            config.write('set ${} {}\n'.format(name, hexcode))
        config.write('\n')
    except Exception as e:
        print('Unable to load theme!')
        raise e

with open(CONF_FILE, 'ab') as config:
    hostname = gethostname()
    copyfileobj(open('base.conf', 'rb'), config)
    config.write(str.encode('\n\n# EXTRA CONFIG FOR *{}*:\n\n'.format(hostname.upper())))
    copyfileobj(open('hosts/{}.conf'.format(hostname), 'rb'), config)

i3 = i3ipc.Connection()
try:
    i3.command('restart')
except Exception as e:
    pass
