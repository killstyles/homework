class dictclass:
	def __init__(self,mydict):
		self.mydict = mydict
	def del_dict(self,key):
		if key in self.mydict:
			self.mydict.pop(key)
			return self.mydict
		else:
			return 'not found'
	def get_dict(self,key):
		if key in self.mydict:
			return key
		else:
			return 'not found'
	def get_key(self):
		return list(self.mydict.keys())
	def update_dict(self,newdict):
		return list(self.mydict.values()) + list(newdict.values())

def main():
	d = {1:0,2:0,3:0,4:0}
	d2 = {99:99}
	d1 = dictclass(d)
	print(d1.del_dict(1))
	print(d1.del_dict(5))
	print(d1.get_dict(2))
	print(d1.get_dict(5))
	print(d1.get_key())
	print(d1.update_dict(d2))
if __name__ == '__main__':
	main()
