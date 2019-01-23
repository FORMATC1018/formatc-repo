import math
class Trapeze():
	def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
	
		def len_side (ax, ay, bx, by):
			return round((math.sqrt((bx-ax)**2 + (by-ay)**2 )), 2)

		self.ax=ax
		self.ay=ay
		self.bx=bx
		self.by=by
		self.cx=cx
		self.cy=cy
		self.dx=dx
		self.dy=dy
		self.len_ab = len_side (self.ax, self.ay, self.bx, self.by)
		self.len_bc = len_side (self.bx, self.by, self.cx, self.cy)
		self.len_cd = len_side (self.cx, self.cy, self.dx, self.dy)
		self.len_ad = len_side (self.ax, self.ay, self.dx, self.dy)
		self.len_diag_ac = len_side (self.ax, self.ay, self.cx, self.cy)
		self.len_diag_bd = len_side (self.bx, self.by, self.dx, self.dy)
	
	def perimetr(self):
		self.perimetr = self.len_ab + self.len_bc + self.len_cd + self.len_ad
		return (self.perimetr)

	def istrapeze(self):
		if self.len_diag_bd==self.len_diag_ac:
			return True
		else:
			return False
	def vysota(self):
		self.h = round((math.sqrt(self.len_ab**2 - ((self.len_ad - self.len_bc)**2)/4)),2)
		return (self.h)
	def ploshad (self):
		return round((((self.len_ad + self.len_bc)/2)*self.h),2)	


trapeze_1 = Trapeze (2,3,4,9,9,9,11,3)
if trapeze_1.istrapeze():
	print("Это трапеция? ", trapeze_1.istrapeze())
	print("Периметр - ",trapeze_1.perimetr())
	print("Высота - ",trapeze_1.vysota())
	print("Площадь - ",trapeze_1.ploshad())
else:
	print ("Это не трапеция")




