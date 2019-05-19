# INA260
Texas Instruments INA260 Python driver

INA260_MINIMAL.py is a bare-bones driver for requesting voltage and current values. It was purposefully made as short as possible.

ina260_logging_example.py is a example of a logging scheme where samples are taken every second and displayed on the screen and to a logfile. To stop the program and close the logfile, ctrl-c needs to be pressed.

The INA260 has the 2 milli ohm sense/shunt resistor inside the chip package, which means that no manual calibration is needed (it is needed for INA219 and INA233 as they have an external resistor). This makes INA260 ideal for hobbists... a simple software driver and a very low sense impedance (will not impact the current that you are measuring).
