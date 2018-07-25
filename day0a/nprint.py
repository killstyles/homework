import sys
def npr(f,n):
	f1 = open(f)
	s = ''
	for i in range(n):
		s += f1.readline()
	print(s)
	return s

def main(): 
    sa = sys.argv
    if len(sa) != 3:
        print('There should be 2 parameters')
    else:
        npr(sa[1],int(sa[2]))
if __name__ == '__main__':
    main()
        

