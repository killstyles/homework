import StuDao
from StuClass import Student
import StuInfo_system
def main():
    while True:
        try:
            StuInfo_system.WelcomeUI()
            user = eval(input('请按照序号进行操作：'))
            if user == 0:
                print('欢迎来到学生信息管理系统'.center(50, '*'))
                print('感谢你的使用！')
                break
            elif user == 1:
                StuInfo_system.SelectUI()
            elif user == 2:
                StuInfo_system.InsertUI()
            elif user == 3:
                StuInfo_system.DelUI()
            elif user == 4:
                StuInfo_system.UpdateUI()
            elif user == 5:
                StuInfo_system.LookUI()
            else:
                continue
        except:
            continue
if __name__ == '__main__':
    main()