def main():
	l = []
	chess(l)
def isab(a,b)
	if a == b == 1:
		return 1
	elif a == b == 2:
		return 2
	else:
		return 0
def win(l):
	for i in range(3):
		if reduce(isab,l[i::3]):
			return reduce(isab,l[i::3])
		elif reduce(isab,l[3 * i:3 * (i + 1):]):
			return True
		elif i==0 and reduce(isab,l[i::4]):
			return reduce(isab,l[i::4])
		elif i==2 and reduce(isab,l[i::2]:
			return reduce(isab,l[i::2]
		else:
			return False
	
def npc(l):
	pass
def pc(l):
	while True:
		pc = eval(input('please input a 0~8:'))
		if l[pc] == 0:
			l[pc] = 1
			break
		else:
			print('There are already pieces in this position!')
			continue
			
def chess_print(l):
	for i in range(0,9,3):
		print(l[i:i + 3])
				
def chess(l):
	for i in range(9):
		l.append(0)
	return l
