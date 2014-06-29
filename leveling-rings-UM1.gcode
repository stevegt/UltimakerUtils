
M107                            ;start with the fan off
G21                             ;metric values
G90                             ;absolute positioning
M82                             ;set extruder to absolute mode
M107                            ;start with the fan off
G28 X0 Y0                       ;move X/Y to min endstops
G28 Z0                          ;move Z to min endstops
G1 Z15.0 F9000                  ;move the platform down 15mm
M140 S60.00                   ;set bed temp (no wait)
M109 T0 S230.00             ;set extruder temp (wait)
G92 E0                          ;zero the extruded length
G1 F200 E3                      ;extrude 3mm of feed stock
G92 E0                          ;zero the extruded length again
G1 F9000                        ;set speed to 9000
;Put printing message on LCD screen
M117 Printing...

;Layer count: 1
;LAYER:0


G0 F9000 X12.50  Y102.50 Z0.15
G2 F1000  X12.50  Y102.50 I90.00 E5.04
G0 F9000 X12.90  Y102.50 Z0.15
G2 F1000  X12.90  Y102.50 I89.60 E10.06
G0 F9000 X13.30  Y102.50 Z0.15
G2 F1000  X13.30  Y102.50 I89.20 E15.06
G0 F9000 X13.70  Y102.50 Z0.15
G2 F1000  X13.70  Y102.50 I88.80 E20.04
G0 F9000 X14.10  Y102.50 Z0.15
G2 F1000  X14.10  Y102.50 I88.40 E24.99
G0 F9000 X14.50  Y102.50 Z0.15
G2 F1000  X14.50  Y102.50 I88.00 E29.92
G0 F9000 X14.90  Y102.50 Z0.15
G2 F1000  X14.90  Y102.50 I87.60 E34.83
G0 F9000 X15.30  Y102.50 Z0.15
G2 F1000  X15.30  Y102.50 I87.20 E39.72
G0 F9000 X15.70  Y102.50 Z0.15
G2 F1000  X15.70  Y102.50 I86.80 E44.58
G0 F9000 X16.10  Y102.50 Z0.15
G2 F1000  X16.10  Y102.50 I86.40 E49.42

;End GCode
M104 S0                         ;extruder heater off
G91                             ;relative positioning
G1 E-1 F300                     ;retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F9000    ;move Z up a bit and retract filament even more
G28 X0 Y0                       ;move X/Y to min endstops, so the head is out of the way
M84                             ;steppers off
G90                             ;absolute positioning
