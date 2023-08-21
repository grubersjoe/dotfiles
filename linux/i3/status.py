#!/usr/bin/env python3

import locale
from i3pystatus import Status, get_module
from subprocess import call
from os.path import expanduser

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

FONTS = {
    'sans': {
        'typeface': 'RobotoCondensed 14',
        'rise': 0
    },
    'mono': {
        'typeface': 'RobotoMono 12',
        'rise': 0
    },
    'icon': {
        'typeface': 'Material Icons 13',
        'rise': -2500
    }
}

THEME = {
    'base00': '#1C2023',
    'base01': '#393F45',
    'base02': '#565E65',
    'base03': '#747C84',
    'base04': '#ADB3BA',
    'base05': '#C7CCD1',
    'base06': '#DFE2E5',
    'base07': '#F3F4F5',
    'base08': '#C7AE95',
    'base09': '#C7C795',
    'base0A': '#AEC795',
    'base0B': '#95C7AE',
    'base0C': '#95AEC7',
    'base0D': '#AE95C7',
    'base0E': '#C795AE',
    'base0F': '#C79595',
    "base005": "#2B3034"
}


def spacer(width=2):
    return font((' ' * width), 'mono')


def font(contents, font='mono', color=''):
    if font in FONTS.keys():
        typeface = str(FONTS[font]['typeface'])
        rise = str(FONTS[font]['rise'])
        if isinstance(color, str) and len(color) > 0:
            color = 'fgcolor="{}"'.format(color)
        span = '<span font="{}" rise="{}" {}>'.format(typeface, rise, color)

        return span + contents + '</span>'
    else:
        return contents


@get_module
def xkblayout_leftclick(self):
    self.change_layout()
    call(['xmodmap', expanduser('~/.Xmodmap')])


status = Status(standalone=True)

status.register(
    'clock',
    format=font('\ue878', 'icon', THEME['base0C']) + font(' %a %-d. %B %H:%M', 'sans') + spacer(1),
    hints={'markup': 'pango'},
)

status.register(
    'xkblayout',
    format=font('\ue312', 'icon', THEME['base0C']) + font(' ', 'sans') + font('{name}') + spacer(),
    hints={'markup': 'pango'},
    uppercase=False,
    layouts=['us', 'de'],
    on_leftclick=[xkblayout_leftclick]
)

status.register(
    'pulseaudio',
    format=font('\ue050', 'icon', THEME['base0C']) + font(' ', 'sans') + font('{volume}') + spacer(),
    format_muted=font('\ue04f', 'icon') + font(' ', 'sans') + font('{volume}') + spacer(),
    hints={'markup': 'pango'},
    color_muted='#CC6666',
    multi_click_timeout=0,
)

status.register(
    'uptime',
    format=font('UP ', 'sans', THEME['base0C']) + font('{days}d {hours}h {mins}m') + spacer(),
    hints={'markup': 'pango'},
)

status.register(
    'load',
    format=font('Load ', 'sans', THEME['base0C']) + font('{avg1} {avg5} {avg15}') + spacer(),
    hints={'markup': 'pango'},
    critical_limit=5.5,
)

status.register(
    'mem',
    format=font('MEM ', 'sans', THEME['base0C']) + font('{percent_used_mem}') + font('%', 'mono') + spacer(),
    hints={'markup': 'pango'},
    divisor=1024 ** 3,
    color=THEME['base05'],
    warn_color=THEME['base09'],
    alert_color=THEME['base0F'],
    round_size=None,
    warn_percentage=70,
    alert_percentage=80,
    interval=1  # does not update otherwise. bug?
)

status.register(
    'cpu_usage',
    format=font('CPU ', 'sans', THEME['base0C']) + font('{usage:02}') + font('%', 'mono') + spacer(),
    hints={'markup': 'pango'},
)

status.register(
    'now_playing',
    format=font('{status} {artist} - {title}', 'sans') + spacer(),
    hints={'markup': 'pango'},
    status={
        'stop': font('\ue037', 'icon', THEME['base0C']),
        'pause': font('\ue037', 'icon', THEME['base0C']),
        'play': font('\ue034', 'icon', THEME['base0C'])
    },
    on_leftclick=None,
    on_doubleleftclick='playpause',
)


status.run()
