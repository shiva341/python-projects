class Calculator:
    def __init__(self,a,b=1):
        self.a = a 
        self.b = b
    def __str__(self):
        print('This is a object of calculator with input values {} {}'.format(str(self.a),str(self.b)))
    def  add(self):
        return self.a+self.b 
    def sub(self):
        return self.a - self.b    
    def mul(self):
        return self.a * self.b    
    def div(self):
        return self.a // self.b    
    def pow(self):
        return self.a**self.b  
    def fac(self):
        op=1
        for i in range(1,(self.a)+1):
            op=op*i  
        return op 
input_1= int(input('Enter the first value:'))
input_2=int(input('Enter the second value:'))
p= Calculator(input_1,input_2)
print(p.fac())


