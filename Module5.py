#Module 5 Assignment

#Creating a class for Point so it is identifiable later on
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Rectangle:
	""" A class to manufacture rectangle objects """
 
	def __init__(self, posn, w, h):
		""" Initialize rectangle at posn, with width w, height h """
		self.corner = posn
		self.width = w
		self.height = h

	def __str__(self):
		return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

#Creating rectangle
def create_rectangle(x,y,w,h):
	return Rectangle(Point(x,y),w,h)

#Stringing rectangle
def str_rectangle(r):
	return "({0},{1},{2},{3})".format(r.corner.x,r.corner.y,r.width,r.height)

#Shifting rectangle
def shift_rectangle(r, dx, dy):
	r.corner=Point(dx,dy)

#Offsetting rectangle
def offset_rectangle(r1,dx,dy):
	return Rectangle(Point(r1.corner.x+dx,r1.corner.y+dy),r1.width,r1.height)

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)

#Testing the previous function
r1 = create_rectangle(10, 20, 30, 40)
print (str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print (str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print (str_rectangle(r1)) # should be same as previous
print (str_rectangle(r2))
