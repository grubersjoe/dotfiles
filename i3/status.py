import subprocess
import locale

from i3pystatus import Status

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

fonts = {
    'fixed': 'Meslo LG M DZ 11',
    'icon': 'FontAwesome 12'
}

def format(contents, type = 'fixed'):
    if type in fonts.keys():
        return '<span font="' + fonts[type] + '">' + contents + '</span>'
    else:
        return contents

status = Status(standalone = True)

status.register('clock',
    format = '%a %-d. %B %H:%M',
)

status.register('xkblayout', 
    format = format('\uf11c', 'icon') + ' ' + format('{name}'),
    uppercase = False,
    layouts = ['us', 'de'],
    hints = {'markup': 'pango'},
)

status.register('pulseaudio',
    format = format('\uf028', 'icon') + ' ' + format('{volume}') + '  ',
    format_muted = format('\uf026', 'icon') + ' ' + format('{volume}') + '  ',
    color_muted = '#CC6666',
    hints = {'markup': 'pango'},
    multi_click_timeout = 0
)

status.register('uptime',
    format = 'UP ' + format('{days}d {hours}h {mins}m') + '  ',
    hints = {'markup': 'pango'},
)

status.register('load',
    format = 'Load ' + format('{avg1} {avg5} {avg15}') +  '  ',
    critical_limit = 5.5,
    hints = {'markup': 'pango'},
)

status.register('mem',
    format = 'MEM ' + format('{percent_used_mem}') + '%  ',
    divisor = 1024**3,
    color = '#ffffff',
    round_size = None,
    warn_percentage = 70,
    alert_percentage = 85,
    hints = {'markup': 'pango'},
)

status.register('cpu_usage',
    format = 'CPU ' + format('{usage:02}') + '%  ',
    hints = {'markup': 'pango'},
)

status.register('spotify',
    format = format('\uf025', 'icon') + '  {artist} - {title}  ',
    format_not_running = '',
    hints = {'markup': 'pango'},
	on_leftclick = None,
	on_doubleleftclick = 'playpause',
)

status.run()
