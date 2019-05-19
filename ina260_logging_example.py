#!/usr/bin/python
from __future__ import print_function
from INA260_MINIMAL import INA260
import time
from datetime import datetime

def main():
	ina260 = INA260(dev_address=0x44);
	ina260.reset_chip()
	time.sleep(1)

	log = open('/home/pi/sample_charging_profile.txt','w')
	print("Time,Bus Voltage (Volts),Charge Current (Amps)")
	print("Time,Bus Voltage (Volts),Charge Current (Amps)", file = log)
	try:
		while True:
			bus_voltage = ina260.get_bus_voltage()
			charge_current = ina260.get_current()
			curtime = datetime.now().strftime("%b %d %Y %H:%M:%S")
			print("%s,%02f,%02f" % (curtime,bus_voltage,charge_current))
			print("%s,%02f,%02f" % (curtime,bus_voltage,charge_current), file = log)
			dt = datetime.now()
			time_to_sleep = 1.0 - (dt.microsecond * 0.000001)
			time.sleep(time_to_sleep)
	except KeyboardInterrupt:
		log.close()
	
if __name__ == '__main__':  
   main()
