#!/usr/bin/env python3

import i3ipc
import json

from os import path
from socket import gethostname
from shutil import copyfileobj


def get_path(filename):
    return path.join(path.dirname(__file__), filename)

i3conf = get_path('config')

# load the theme file and append it's colors to i3 as variables
with open(i3conf, 'w') as config:
    try:
        with open(get_path('../theme/theme.json')) as t:
            theme = json.load(t)

        config.write('# THEME\n')
        for name, hexcode in theme.items():
            config.write('set ${} {}\n'.format(name, hexcode))
        config.write('\n')
    except Exception as e:
        print('Unable to load theme!')
        raise e

# add the remaining config files
with open(i3conf, 'ab') as config:
    copyfileobj(open(get_path('base.conf'), 'rb'), config)

    hostname = gethostname()
    hostconf = get_path('hosts/{}.conf'.format(hostname))
    title = str.encode('\n\n# EXTRA CONFIG FOR *{}*:\n\n'.format(hostname.upper()))
    config.write(title)
    copyfileobj(open(hostconf, 'rb'), config)

# reload i3 
i3 = i3ipc.Connection()
i3.command('reload')
