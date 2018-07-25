import sys
import os
def myfind(f,p):
	os.chdir(p)
	op = os.path
	for i in os.listdir(p):
		if  f == p and not(op.isdir(p)):
			return True
		elif op.isdir(p):	
			if myfind(f,op.join(p,i)) == True:
				return True
			else:
				os.chdir(os.pardir(i))
	return False
def main():
    sa = sys.argv
    if len(sa) != 3:
        print('There should be 2 parameters')
    else:
        print(myfind(sa[1],sa[2]))
if __name__ == '__main__':
    main()
