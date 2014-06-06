#!/usr/bin/python

rings = 10
# wide = 0.4
wide = 0.8
thick = .1
base_dia = 150
center_x = 230/2.0
center_y = 225/2.0

pi=3.1415927

head = ''';FLAVOR:UltiGCode
;MATERIAL:{total_mm3:.0f}

;Layer count: 1
;LAYER:0
M107
G11
'''

loop = '''
G0 F9000 X{x:.2f}  Y{y:.2f} Z{z:.2f}
G2 F1000  X{x:.2f}  Y{y:.2f} I{r:.2f} E{total_mm3:.2f}
'''

loop_retract = '''
G11
G0 F9000 X{x:.2f}  Y{y:.2f} Z{z:.2f}
G2 F1000  X{x:.2f}  Y{y:.2f} I{r:.2f} E{total_mm3:.2f}
G10
G0 Z1
'''

tail = '''
M107
G0 F15000 X97.69 Y88.49 Z85.00
M25
'''

total_mm3 = 0

body = ''
for i in range(rings):
	dia = base_dia + wide * 2 * i
	cross_section = thick * wide
	circumference = pi * dia 
	r = dia/2.0;
	x = center_x - r
	y = center_y 
	z = thick
	mm3 = circumference * cross_section
	total_mm3 += mm3
	body += loop.format(**vars())


print head.format(**vars())
print body.format(**vars())
print tail.format(**vars())
