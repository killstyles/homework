class Student:
	def __init__(self,name,age,course):
		self.name = name
		self.age = age
		self.course = course
	def get_name(self):
		return self.name
	def get_age(self):
		return int(self.age)
	def get_course(self):
		return int(max(self.course)) 
	def	Student(self):
		return Student.get_name(self),Student.get_age(self),Student.get_course(self)

def main():
	zm = Student('zhangming',20,[69,88,100])
	print(zm.Student())
if __name__ == '__main__':
	main()
	
		
