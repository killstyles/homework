import sys
def cpabc(fd1,fd2,fd3):
	cp1 = open(fd1)
	cp2 = open(fd2,'w+')
	cnt = 0
	while True:
		ff = cp1.readline()
		cnt += 1
		if ff  == '':
			break
		elif cnt == 3:
			cp2.write(fd3)
			cp2.write(ff)
		else:
			cp2.write(ff)
	cp1.close()
	cp2.close()
	return 0
if __name__ == '__main__':
	sa = sys.argv
	if len(sa) != 4:
		print('There should be 3 parameters')
	else:
		cpabc(sa[1],sa[2],sa[3])
