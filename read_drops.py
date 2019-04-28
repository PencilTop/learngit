#!/bin/env python3

def read_devices(devices_txt):
	try:
		with open(devices_txt) as dev:
			for l in dev.readlines():
				yield l.strip()
	except Exception as e:
		print(e)
		print("File {} not found".format(devices_txt))




if __name__ == '__main__':
	print(list(read_devices('devices_txt')))
