#coding=utf-8
def myfunc():
   a = 1;
   b = 2;
   sum = a + b;
   return sum;

import dis
dis.dis(myfunc)
