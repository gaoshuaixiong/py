class Foo(object):
	def __init__(self):
		print("__init__ in")
	def ord_func(self):
		pass
		print("普通方法")
	@classmethod
	def class_func(cls):
		pass
		print("类方法")
	@staticmethod
	def static_func():
		pass
		print("静态方法")

f = Foo()
f.ord_func()

Foo.class_func()
Foo.static_func()