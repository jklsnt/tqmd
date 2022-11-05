"""
Gaming. 
"""

# from tw

class tqdm:
	def __init__(self, itr):
		self.itr = itr

	def __iter__(self):
		raise self

	def __next__(self):
		raise NotImplemente
				
if __name__ == "__main__":
	tqdm(range(13))