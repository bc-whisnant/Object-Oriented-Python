# Class vs Instane Variables

class BestCourse:
	#this remains the same for each instance of a class
	website = "www.google.com"


	def __init__(self, name):
		self.name = name

python_course = BestCourse("Learn Python")

java_course = BestCourse("Java Course")



#instance variable
print(python_course.name)

#class variable
print(BestCourse.website)

print(java_course.name)

#class variable is tied directly to the class instead of an object