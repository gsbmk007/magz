import matplotlib as ml
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Light():
	def __init__(self, brightness, color, pos, size):
		self.b = brightness
		self.pos = pos
		self.size = size
		self.color = self.define_color(color)
		self.circle = self.construct_circle()

	def define_color(self, new_color):
		if (type(new_color) == str):
			color = ml.colors.to_rgb(new_color)
		else:
			color = new_color
		return(color)
	
	def set_brightness(self, new_brightness):
		self.b = new_brightness

	def set_color(self, new_color):
		self.color = self.define_color(new_color)
	
	def set_pos(self, new_pos):
		self.pos = new_pos

	def set_size(self,new_size):
		self.size = new_size

	def construct_circle(self):
		return(patches.Circle([self.pos[0],self.pos[1]], self.size[0], facecolor=[*self.color, 1]))

	def construct_light(self,stgsize):
		return(patches.Rectangle([self.pos[0]-self.size[0],stgsize-self.size[1]], 2*self.size[0], self.size[1], facecolor=[*self.color, 1]))

	def construct_beam(self,stgsize):
		x = [self.pos[0]+self.size[0],self.pos[0]-self.size[0],self.pos[0]-self.size[0]-self.size[2],self.pos[0]+self.size[0]+self.size[2]]
		y = [stgsize,stgsize,0,0]
		return(patches.Polygon(xy=list(zip(x,y)), fill=True, facecolor=[*self.color, self.b]))


