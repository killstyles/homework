class Student(object):
    def __init__(self,sno='',sname='',sex='',sgrade=''):
        self.sno = sno
        self.sname = sname
        self.sex = sex
        self.sgrade = sgrade
    def setSno(self,sno):
        self.sno = sno
    def getSno(self):
        return self.sno
    def setSname(self,sname):
        self.sname = sname
    def getSname(self):
        return self.sname
    def setSex(self,sex):
        self.sex = sex
    def getSex(self):
        return self.sex
    def setSgrade(self,sgrade):
        self.sgrade = sgrade
    def getSgrade(self):
        return self.sgrade
    def toString(self):
        return 'Student{' + 'sno=' + self.sno + ', sname=' + self.sname + \
               ', sex=' + self.sex+ ', sgrade=' + self.sgrade + '}'