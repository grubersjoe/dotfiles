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

COLORS = {
    "Background"  : "#1d1f21",
    "CurrentLine" : "#282a2e",
    "Selection"   : "#373b41",
    "Foreground"  : "#c5c8c6",
    "Comment"     : "#969896",
    "Red"         : "#cc6666",
    "Orange"      : "#de935f",
    "Yellow"      : "#f0c674",
    "Green"       : "#b5bd68",
    "Aqua"        : "#8abeb7",
    "Blue"        : "#81a2be",
    "Blue"        : "#b294bb"
}   



def spacer(width=2):
    return font((' ' * width), 'mono')


def font(contents, font='mono', color=''):
    if font in FONTS.keys():
        typeface = str(FONTS[font]['typeface'])
        rise = str(FONTS[font]['rise'])
        if isinstance(color, str) and len(color) > 0: color = 'fgcolor="{}"'.format(color)
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
    format=font('\ue878', 'icon') + font(' %a %-d. %B %H:%M', 'sans') + spacer(1),
    hints={'markup': 'pango'},
)

status.register(
    'xkblayout',
    format=font('\ue312', 'icon') + font(' ', 'sans') + font('{name}') + spacer(),
    hints={'markup': 'pango'},
    uppercase=False,
    layouts=['us', 'de'],
    on_leftclick=[xkblayout_leftclick]
)

status.register(
    'pulseaudio',
    format=font('\ue050', 'icon') + font(' ', 'sans') + font('{volume}') + spacer(),
    format_muted=font('\ue04f', 'icon') + font(' ', 'sans') + font('{volume}') + spacer(),
    hints={'markup': 'pango'},
    color_muted='#CC6666',
    multi_click_timeout=0,
)

status.register(
    'uptime',
    format=font('UP ', 'sans', COLORS['Blue']) + font('{days}d {hours}h {mins}m') + spacer(),
    hints={'markup': 'pango'},
)

status.register(
    'load',
    format=font('Load ', 'sans', COLORS['Blue']) + font('{avg1} {avg5} {avg15}') + spacer(),
    hints={'markup': 'pango'},
    critical_limit=5.5,
)

status.register(
    'mem',
    format=font('MEM ', 'sans', COLORS['Blue']) + font('{percent_used_mem}') + font('%', 'mono') + spacer(),
    hints={'markup': 'pango'},
    divisor=1024 ** 3,
    color='#ffffff',
    warn_color='#f0c674',
    alert_color='#cc6666',
    round_size=None,
    warn_percentage=70,
    alert_percentage=80,
    interval=1 # does not update otherwise. bug?
)

status.register(
    'cpu_usage',
    format=font('CPU ', 'sans', COLORS['Blue']) + font('{usage:02}') + font('%', 'mono') + spacer(),
    hints={'markup': 'pango'},
)

status.register(
    'now_playing',
    format=font('{status} {artist} - {title}', 'sans') + spacer(),
    hints={'markup': 'pango'},
    status={
        'stop': font('\ue037', 'icon'),
        'pause': font('\ue037', 'icon'),
        'play': font('\ue034', 'icon')
    },
    on_leftclick=None,
    on_doubleleftclick='playpause',
)


status.run()
