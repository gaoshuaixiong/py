import ctypes 
ll = ctypes.cdll.LoadLibrary  
lib = ll("./timeTester.so")   
lib.get(10000) 
print('***finish***') 
