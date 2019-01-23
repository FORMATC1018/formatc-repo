import math
class Triangle():
	def __init__(self, ax, ay, bx, by, cx, cy):
		self.ax=ax
		self.ay=ay
		self.bx=bx
		self.by=by
		self.cx=cx
		self.cy=cy
		self.ab = round((math.sqrt((self.bx-self.ax)**2 + (self.by-self.ay)**2 )), 2)
		self.bc = round((math.sqrt((self.cx-self.bx)**2 + (self.cy-self.by)**2 )), 2)
		self.ac = round((math.sqrt((self.cx-self.ax)**2 + (self.cy-self.ay)**2 )), 2)
	def perimetr(self):
		self.perimetr = self.ab + self.bc + self.ac
		return (self.perimetr)

	def ploshad (self):
		self.p = self.perimetr/2
		self.ploshad = round(math.sqrt(self.p*(self.p - self.ab)*(self.p - self.bc)* (self.p - self.ac)),2)
		return (self.ploshad)

	def vysota (self):
		self.vysota = round(((self.ploshad*2)/self.ac),2)
		return (self.vysota)

triangle_1 = Triangle (1,1,2,2,3,3)
print("Периметр - ", triangle_1.perimetr())
print("Площадь - ",triangle_1.ploshad())
print("Высота - ",triangle_1.vysota())