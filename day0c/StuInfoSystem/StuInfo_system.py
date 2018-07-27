from StuClass import Student
import StuDao
stu = Student
def WelcomeUI():
    print('欢迎来到学生信息管理系统'.center(50,'*'))
    print('查询学生信息：1')
    print('添加学生信息：2')
    print('删除学生信息：3')
    print('修改学生信息：4')
    print('查看所有学生信息：5')
    print('退出：0')
def SelectUI():
    print('欢迎来到学生信息管理系统'.center(50, '*'))
    mysno = input('请输入您要查询的学号：')

    StuDao.SelectStu(mysno)
def InsertUI():
    print('欢迎来到学生信息管理系统'.center(50, '*'))
    mysno = input('请输入您要添加的学生的学号：')
    mysname = input('请输入您要添加的学生的姓名：')
    mysex = input('请输入您要添加的学生的性别：')
    mysgrade = input('请输入您要添加的学生的年级：')
    StuDao.InsertStu(mysno,mysname,mysex,mysgrade)
def DelUI():
    print('欢迎来到学生信息管理系统'.center(50, '*'))
    StuDao.Lookstu()
    mysno = eval(input('请输入您要删除的学号：'))
    StuDao.DelStu(mysno)
def UpdateUI():
    print('欢迎来到学生信息管理系统'.center(50, '*'))
    mysno = input('请输入您要修改学生信息的学号：')
    StuDao.SelectStu(mysno)
    mysname = input('请输入您要修改的姓名：')
    mysex = input('请输入您要修改的性别：')
    mysgrade= input('请输入您要修改的年级：')
    StuDao.UpdateStu( mysno,mysname,mysex,mysgrade)
def LookUI():
    print('欢迎来到学生信息管理系统'.center(50, '*'))
    StuDao.Lookstu()
