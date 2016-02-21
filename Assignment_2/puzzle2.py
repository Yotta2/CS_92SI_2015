import collections

# Solution 1: use namedtuple
# Direction = collections.namedtuple('Direction', ['x_delta', 'y_delta', 'dir'])

# instructions = input("instructions(a string consisting of a series of letters A, C or S: ")

# dirs = [Direction(0, +1, 'N'),
# 		Direction(+1, +1, 'NE'),
# 		Direction(+1, 0, 'E'),
# 		Direction(+1, -1, 'SE'),
# 		Direction(0, -1, 'S'),
# 		Direction(-1, -1, 'SW'),
# 		Direction(-1, 0, 'W'),
# 		Direction(-1, +1, 'NW')]

# x = 0
# y = 0

# index = 0

# for ins in instructions:
# 	if ins == 'S':
# 		x += dirs[index].x_delta
# 		y += dirs[index].y_delta
# 	elif ins == 'C':
# 		index = (index + 1) % len(dirs)
# 	elif ins == 'A':
# 		index -= 1
# 		if index == -1:
# 			index = len(dirs) - 1

# print("{0},{1}".format((x, y), dirs[index].dir))

# Solution 2: encasulate Direction class
instructions = input("instructions(a string consisting of a series of letters A, C or S: ")

class Direction:
	"""
	Direction class is used to encasulate direction and deal with rotation.
	"""
	Direction_tuple = collections.namedtuple('Direction_tuple', ['x_delta', 'y_delta', 'dir'])
	__dirs__ = [Direction_tuple(0, +1, 'N'),
			Direction_tuple(+1, +1, 'NE'),
			Direction_tuple(+1, 0, 'E'),
			Direction_tuple(+1, -1, 'SE'),
			Direction_tuple(0, -1, 'S'),
			Direction_tuple(-1, -1, 'SW'),
			Direction_tuple(-1, 0, 'W'),
			Direction_tuple(-1, +1, 'NW')]

	def __init__(self):
		"""
		Default facing north.
		TODO: support init direction parameter
		"""
		self.index = 0
		self.x_delta, self.y_delta, self.dir = Direction.__dirs__[self.index]

	def rotate_counterclockwise(self):
		self.index -= 1
		if self.index == -1:
			self.index = len(Direction.__dirs__) - 1
		self.x_delta, self.y_delta, self.dir = Direction.__dirs__[self.index]

	def rotate_clockwise(self):
		self.index = (self.index + 1) % len(Direction.__dirs__)
		self.x_delta, self.y_delta, self.dir = Direction.__dirs__[self.index]

curr_dir = Direction()

x = 0
y = 0

for ins in instructions:
	if ins == 'S':
		x += curr_dir.x_delta
		y += curr_dir.y_delta
	elif ins == 'C':
		curr_dir.rotate_clockwise()
	elif ins == 'A':
		curr_dir.rotate_counterclockwise()

print("{0},{1}".format((x, y), curr_dir.dir))













