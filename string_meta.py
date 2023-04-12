class StringOnlyMeta(type):
	def __call__(cls, *args, **kwargs):
		for arg in args:
			if not isinstance(arg, str):
				raise TypeError("Arguments must be strings")
		return super().__call__(*args, **kwargs)


class MyStringOnlyClass(metaclass=StringOnlyMeta):
	def __init__(self, name, description):
	    self.name = name
	    self.description = description

	    

# This will work because both arguments are strings
obj1 = MyStringOnlyClass("name", "description")

# This will raise a TypeError because the second argument is not a string
obj2 = MyStringOnlyClass("name", 123)



