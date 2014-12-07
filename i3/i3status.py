# -*- coding: utf-8 -*-

import subprocess
import locale

from i3pystatus import Status

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

status = Status(standalone=True)

status.register('clock',
	format='  %a %-d. %B %H:%M KW %V')

status.register('mem',
	format='  {used_mem} / {total_mem} GiB   ',
	divisor=1024**3,
	color='#ffffff',
	round_size=2,
	warn_percentage=60,
	alert_percentage=80)

status.register('cpu_usage',
	format='  {usage:02}% ')

status.register('load',
	format='  {avg1} {avg5} {avg15} ',
	critical_limit=5.5)

status.register('spotify',
	format='♪ {artist} - {title}   ')

# status.register('pulseaudio',
#     format='♪ {volume}')

# Shows your CPU temperature, if you have a Intel CPU
# status.register('temp',
#     format='{temp:.0f}°C',)

status.run()
