# p.py
class P:
    def __init__(self, name, alias):
        self.name = name       # public
        self.__alias = alias   # private
    
    def who(self):
        print('name  : ', self.name)
        print('alias : ', self.__alias)
      
    def __foo(self):          # private method
        print('This is private method')
    def foo(self):            # public method
        print('This is public method')
        self.__foo()
