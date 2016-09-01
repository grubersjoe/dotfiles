import locale
from i3pystatus import Status

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

fonts = {
    'fixed': 'Meslo LG M DZ 11',
    'icon': 'Material Icons 13',
}
icon_rise = -2500


def setfont(contents, font='fixed'):
    if font in fonts.keys():
        if font == 'icon':
            span = '<span font="' + fonts[font] + '" rise="' + str(icon_rise) + '">'
        else:
            span = '<span font="' + fonts[font] + '">'

        return span + contents + '</span>'
    else:
        return contents


status = Status(standalone=True)

status.register(
    'clock',
    format=setfont('\ue8df', 'icon') + ' %a %-d. %B %H:%M',
    hints={'markup': 'pango'},
)

status.register(
    'xkblayout',
    format=setfont('\ue312', 'icon') + ' ' + setfont('{name} '),
    uppercase=False,
    layouts=['us', 'de', 'fr'],
    hints={'markup': 'pango'},
)

status.register(
    'pulseaudio',
    format=setfont('\ue050', 'icon') + ' ' + setfont('{volume}') + '  ',
    format_muted=setfont('\ue04f', 'icon') + ' ' + setfont('{volume}') + '  ',
    color_muted='#CC6666',
    hints={'markup': 'pango'},
    multi_click_timeout=0
)

status.register(
    'uptime',
    format='UP ' + setfont('{days}d {hours}h {mins}m') + '  ',
    hints={'markup': 'pango'},
)

status.register(
    'load',
    format='Load ' + setfont('{avg1} {avg5} {avg15}') + '  ',
    critical_limit=5.5,
    hints={'markup': 'pango'},
)

status.register(
    'mem',
    format='MEM ' + setfont('{percent_used_mem}') + '%  ',
    divisor=1024 ** 3,
    color='#ffffff',
    round_size=None,
    warn_percentage=70,
    alert_percentage=85,
    hints={'markup': 'pango'},
)

status.register(
    'cpu_usage',
    format='CPU ' + setfont('{usage:02}') + '%  ',
    hints={'markup': 'pango'},
)

status.register(
    'spotify',
    format='{status} {artist} - {title}  ',
    format_not_running='',
    status={'paused': setfont('\ue037', 'icon'), 'playing': setfont('\ue034', 'icon')},
    hints={'markup': 'pango'},
    on_leftclick=None,
    on_doubleleftclick='playpause',
)

status.run()
