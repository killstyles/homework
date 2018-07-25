import itertools
import random
def main():
	user = []
	l1 = ['黑桃','红桃','梅花','方片']
	l2 = []
	for i in range(1,14):
		l2.append(i)
	l3 = list(itertools.product(l1,l2))
	print(l3)
	print()
	print(poker_clear(l3))
	print()
	print(mypoker(4,l3,user))
def poker_clear(l):
	for i in range(100):
		for j in range(52):
			a = random.randint(0,51)
			l[j],l[a] = l[a],l[j]
	return l
def mypoker(n,l,myuser):
	for i in range(n):
		myuser.append([])
		myuser[i].append(l[i::n])
	return myuser
if __name__ == '__main__':
	main()
