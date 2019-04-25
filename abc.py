import os, sys

class Hello:
	def __init__(self, name):
		self.name=name
	def waveHand(self):
		print("{} is waving hands.".format(self.name))
	def sayHi(self):
		print("{} is saying hi.".format(self.name))

if __name__=='__main__':
	print('Hello')
	print(os.listdir())
	print(sys.path)
	h = Hello('Kathy')
	h.waveHand()
	h.sayHi()
