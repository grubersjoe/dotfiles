import subprocess
import locale

from i3pystatus import Status

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

status = Status(standalone = True)

status.register('clock',
	format = '%a %-d. %B %H:%M',
	hints = {'markup': 'pango'},
)

status.register('xkblayout', 
	format = '<span font="FontAwesome Normal 12">\uf11c</span> {name}  ',
	uppercase = False,
	layouts = ['us', 'de'],
	hints = {'markup': 'pango'},
)

status.register('pulseaudio',
	format = '<span font="FontAwesome Normal 12"></span> <span font="Fira Mono 13">{volume}</span>  ',
	format_muted = '<span font="FontAwesome Normal 12"></span> <span font="Fira Mono 13">{volume}</span>  ',
	color_muted = '#CC6666',
	hints = {'markup': 'pango'},
)

status.register('uptime',
	format = 'UP <span font="Fira Mono 13">{hours}h {mins}m</span>  ',
	hints = {'markup': 'pango'},
)

status.register('load',
	format = 'Load <span font="Fira Mono 13">{avg1} {avg5} {avg15}</span>  ',
	critical_limit = 5.5,
	hints = {'markup': 'pango'},
)

status.register('mem',
	format = 'MEM <span font="Fira Mono 13">{percent_used_mem}</span>%  ',
	divisor = 1024**3,
	color = '#ffffff',
	round_size = None,
	warn_percentage = 70,
	alert_percentage = 85,
	hints = {'markup': 'pango'},
)

status.register('cpu_usage',
	format = 'CPU <span font="Fira Mono 13">{usage:02}</span>%  ',
	hints = {'markup': 'pango'},
)

status.register('spotify',
	format = '{artist} - {title}  ',
	format_not_running = '',
)

status.run()
