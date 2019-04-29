#!/bin/env python3
import re


def read_devices(devices_txt):
	try:
		with open(devices_txt) as devs:
			for l in devs.readlines():
				yield l.strip()
	except Exception as e:
		print(e)
		print("File {} not found".format(devices_txt))

def read_drops(device, pattern):
	p = re.compile(pattern)
	try:
		with open(device) as dev:
			for l in dev.readlines():
				m = p.match(device) 
				if m is not None:
					yild int(m.group(1))
	except Exception as e:
		print(e)
		print("File {} not found or pattern is wrong".format(device))

if __name__ == '__main__':
	print(list(read_devices('devices_txt')))
	drops_pattern = r'.*Total output drops: (\d+)'
	dropsdic = {}
	for d in read_devices(devices):
		dropsdic[d] = list(read_drops(d, drops_pattern))
