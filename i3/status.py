import subprocess
import locale

from i3pystatus import Status

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

status = Status(standalone = True)

status.register('clock',
	format = '%a %-d. %B %H:%M'
)

status.register('mem',
	format = 'MEM {percent_used_mem}%  ',
	divisor = 1024**3,
	color = '#ffffff',
	round_size = None,
	warn_percentage = 70,
	alert_percentage = 80
)

status.register('cpu_usage',
	format = 'CPU {usage:02}%  '
)

status.register('load',
	format = 'Load {avg1} {avg5} {avg15}  ',
	critical_limit = 5.5
)

status.register('spotify',
	format = '{artist} - {title}   '
)

# status.register('pulseaudio',
#     format = '♪ {volume}')

status.run()
