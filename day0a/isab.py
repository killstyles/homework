import sys
def isab(f1,f2):
	fd1,fd2 = open(f1),open(f2)
	cnt = 0
	while True:
		cnt += 1
		fdr1 = fd1.readline()
		fdr2 = fd2.readline()
		if fdr1 == '' and fdr2 == '':
			break
		elif fdr1 != fdr2:
			print(cnt)
	fd1.close()
	fd2.close()
def main():	
	sa = sys.argv 
	if len(sa) != 3:
		print('There should be 2 parameters')
	else:
		isab(sa[1],sa[2])
if __name__ == '__main__':
	main()
		
