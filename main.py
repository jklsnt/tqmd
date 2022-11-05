"""
Gaming. 
"""
import time
# from tw
import os

import os 

# os get

class tqdm:
	def __init__(self, itr, *args, **kwargs):
		self._iterations = 0
		self._itr = itr

	def __iter__(self):
		return self

	def __next__(self):
		self._iterations += 1
		value = next(self._itr)
		print("".join(['▊█jfhh' for i in range(os.get_terminal_size().columns)]))
		print(f"{['/', '-' '\',][self._iterations % 2]} {self._iterations}", end="\r")
		return value

if __name__ == "__main__":
	for i in tqdm(iter(range(10000))):
		time.sleep(1)