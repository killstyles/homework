from functools import reduce
def main():
	l = []
	chess(l)
	for i in range(9 // 2 + 1):
		pc(l)
		chess_print(l)
		if win(l) == 1:
			print('pc1:win!')
			break
		pc1(l)
		chess_print(l)
		if win(l) == 2:
			print('pc2:win!')
			break
	else:
		print('peace!!')
				
		
def isab(a,b):
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
			return reduce(isab,l[3 * i:3 * (i + 1):])
		elif i == 0 and reduce(isab,l[i::4]):
			return reduce(isab,l[i::4])
		elif i == 2 and reduce(isab,l[i::2]):
			return reduce(isab,l[i::2])
	else:
		return 0
	
def npc(l):
	pass

def pc1(l):
	while True:
		pc1 = eval(input('pc2:please input a 1~9:'))
		if l[pc1-1] == 0:
			l[pc1-1] = 2
			break
		else:
			print('There are already pieces in this position!')
			continue

def pc(l):
	while True:
		pc = eval(input('pc1:please input a 1~9:'))
		if l[pc-1] == 0:
			l[pc-1] = 1
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
if __name__ == '__main__':
	main()
