import locale
from i3pystatus import Status, get_module
from subprocess import call
from os.path import expanduser

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

fonts = {
    'sans': {
        'typeface': 'Fira Sans Regular 13',
        'rise': 0
    },
    'mono': {
        'typeface': 'Meslo LG M DZ 11',
        'rise': 0
    },
    'icon': {
        'typeface': 'Material Icons 13',
        'rise': -2500
    }
}


def spacer(width=6):
    return '<span font="Fira Sans Regular 6">' + (' ' * width) + '</span>'


def font(contents, font='mono'):
    if font in fonts.keys():
        span = '<span font="' + str(fonts[font]['typeface']) + '" rise="' + str(fonts[font]['rise']) + '">'

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
    format=font('\ue878', 'icon') + font(' %a %-d. %B %H:%M', 'sans'),
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
    format=font('UP ', 'sans') + font('{days}d {hours}h {mins}m') + spacer(),
    hints={'markup': 'pango'},
)

status.register(
    'load',
    format=font('Load ', 'sans') + font('{avg1} {avg5} {avg15}') + spacer(),
    hints={'markup': 'pango'},
    critical_limit=5.5,
)

status.register(
    'mem',
    format=font('MEM ', 'sans') + font('{percent_used_mem}') + font('%', 'sans') + spacer(),
    hints={'markup': 'pango'},
    divisor=1024 ** 3,
    color='#ffffff',
    round_size=None,
    warn_percentage=70,
    alert_percentage=80,
    interval=1 # does not update otherwise. bug?
)

status.register(
    'cpu_usage',
    format=font('CPU ', 'sans') + font('{usage:02}') + font('%', 'sans') + spacer(),
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
