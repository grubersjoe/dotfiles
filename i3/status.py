import locale
from i3pystatus import Status, get_module
from subprocess import call
from os.path import expanduser

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

fonts = {
    'sans': 'Fira Sans Regular 13',
    'mono': 'Meslo LG M DZ 11',
    'icon': 'Material Icons 13',
}
icon_rise = -2500


def spacer(width=6):
    return '<span font="Fira Sans Regular 6">' + (' ' * width) + '</span>'

def font(contents, font='mono'):
    if font in fonts.keys():
        if font == 'icon':
            span = '<span font="' + fonts[font] + '" rise="' + str(icon_rise) + '">'
        else:
            span = '<span font="' + fonts[font] + '">'

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
    uppercase=False,
    layouts=['us', 'de'],
    hints={'markup': 'pango'},
    on_leftclick=[xkblayout_leftclick]
)

status.register(
    'pulseaudio',
    format=font('\ue050', 'icon') + font(' ', 'sans') + font('{volume}') + spacer(),
    format_muted=font('\ue04f', 'icon') + font(' ', 'sans') + font('{volume}') + spacer(),
    color_muted='#CC6666',
    hints={'markup': 'pango'},
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
    critical_limit=5.5,
    hints={'markup': 'pango'},
)

status.register(
    'mem',
    format=font('MEM ', 'sans') + font('{percent_used_mem}') + font('%', 'sans') + spacer(),
    divisor=1024 ** 3,
    color='#ffffff',
    round_size=None,
    warn_percentage=70,
    alert_percentage=85,
    hints={'markup': 'pango'},
)

status.register(
    'cpu_usage',
    format=font('CPU ', 'sans') + font('{usage:02}') + font('%', 'sans') + spacer(),
    hints={'markup': 'pango'},
)

status.register(
    'now_playing',
    format=font('{status} {artist} - {title}', 'sans') + spacer(),
    status={
        'stop': font('\ue037', 'icon'),
        'pause': font('\ue037', 'icon'),
        'play': font('\ue034', 'icon')
    },
    hints={'markup': 'pango'},
    on_leftclick=None,
    on_doubleleftclick='playpause',
)


status.run()
