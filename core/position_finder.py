from subprocess import run
from sys import argv
from pathlib import Path

script = Path(argv[0]).name

a = run('cmdow /t /p /f /b', capture_output=True, shell=True).stdout.strip().decode('utf8', 'replace').splitlines()
a = [ i.split() for i in a ]
a = [ [*row[:12], ' '.join(row[12:])] for row in a ]

for i in a:
	image, caption = i[-2:]
	x, y, w, h = i[7:11]

	t = caption.split(' - ')
	if len(t)>1 and script in t[-1]:
		continue
	print(f'{caption} :: Size: [{w}, {h}] Pos: [{x}, {y}]')

