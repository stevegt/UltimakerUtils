#!/usr/bin/python

# Derived from the UM2 version by an anonymous contributor...
#
# http://umforum.ultimaker.com/index.php?/topic/5951-um2-calibration-utility-leveling-ringsgcode/?p=54694
#
# ...who wisely says:  "I accept NO liability for any damage done by
# using either version or any derivatives.   USE AT YOUR OWN RISK."  

filament_diameter = 2.89
build_area_width = 205.0
build_area_depth = 205.0
rings = 10
wide = 0.4
thick = 0.2925 / 2

temperature = 230
bed_temperature = 60

base_dia = 180

pi=3.1415927

center_x = build_area_width/2.0
center_y = build_area_depth/2.0

filament_area = (filament_diameter / 2) ** 2 * pi

head = '''
M107                            ;start with the fan off
G21                             ;metric values
G90                             ;absolute positioning
M82                             ;set extruder to absolute mode
M107                            ;start with the fan off
G28 X0 Y0                       ;move X/Y to min endstops
G28 Z0                          ;move Z to min endstops
G1 Z15.0 F9000                  ;move the platform down 15mm
M140 S{bed_temperature:.2f}                   ;set bed temp (no wait)
M109 T0 S{temperature:.2f}             ;set extruder temp (wait)
M190 S{bed_temperature:.2f}                ;set bed temp (wait)
G92 E0                          ;zero the extruded length
G1 F200 E3                      ;extrude 3mm of feed stock
G92 E0                          ;zero the extruded length again
G1 F9000                        ;set speed to 9000
;Put printing message on LCD screen
M117 Printing...

;Layer count: 1
;LAYER:0
'''

loop = '''
G0 F9000 X{x:.2f}  Y{y:.2f} Z{z:.2f}
G2 F1000  X{x:.2f}  Y{y:.2f} I{r:.2f} E{total_mm3:.2f}'''

tail = '''
;End GCode
M104 S0                         ;extruder heater off
M140 S0                         ;heated bed heater off (if you have it)
G91                             ;relative positioning
G1 E-1 F300                     ;retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F9000    ;move Z up a bit and retract filament even more
G28 X0 Y0                       ;move X/Y to min endstops, so the head is out of the way
M84                             ;steppers off
G90                             ;absolute positioning'''

total_mm3 = 0

body = ''

cross_section = thick * wide
z = thick

for i in range(rings):
	dia = base_dia - ((wide * 2) * i)
	circumference = pi * dia 
	r = dia/2.0;
	x = center_x - r
	y = center_y 
	mm3 = (circumference * cross_section) / filament_area
	total_mm3 += mm3
	body += loop.format(**vars())

print head.format(**vars())
print body
print tail.format(**vars())
