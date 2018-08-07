class Stack():
    def __init__(self):
        self.__sk = []
    def press(self,pr):
        self.__sk.append(pr)
        print(self.__sk)
    def push(self):
        try:
            self.po = self.__sk.pop()
            print(self.__sk)
            return self.po
        except IndexError as e:
            print('stack is empty')
            return 0
    def empty(self):
        if not self.__sk:
            print('stack is empty')
            return 0
if __name__ == '__main__':
    stack1 =Stack()
    stack1.press(1)
    stack1.press(2)
    stack1.press(3)
    stack1.push()
    stack1.push()
    stack1.push()
    stack1.push()
    stack1.empty()