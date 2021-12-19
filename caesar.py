import re

class Caeser:
    def __init__(self, msg, key):
        self.msg = msg
        self.key = key
        self.domin = r'[a-zA-Z]'
        self.temp0 = re.findall(self.domin, self.msg)
        self.temp1 = ''
    def encrypt(self):
       
        for i in self.msg:
            if i in self.temp0:
                self.temp1 += chr(ord(i) + self.key)
            else:
                self.temp1 += i
        self.msg = self.temp1
        return self.temp1

    def decrypt(self):
        self.temp0 = re.findall(self.domin, self.msg) 
        self.temp1 = '' 
        for j in self.msg:
            if j in self.temp0:
                self.temp1 += chr(ord(j) - self.key)
            else:
                self.temp1 += j
        
        return self.temp1



