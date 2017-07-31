#-*- coding: utf-8 -*-


class Matrix(object):
	''' Class implementation'''
	def __init__(self, mat):
		self.mat = mat # mat: 2-D list
		self.row = len(self.mat)
		self.col = len(self.mat[0])

	def dot(self, b):
		'''b: Matrix object'''
		if self.col != b.row:
			raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (self.row, self.col, b.row, b.col))

		out = [[0 for n in xrange(b.col)] for m in xrange(self.row)]

		for j in xrange(b.row):
			for i in xrange(self.row):
				for k in xrange(self.col):
					out[i][j] += self.mat[i][k]*b.mat[k][j]

		return Matrix(out)

	def transpose(self):
		transposed = [[0 for m in xrange(self.row)] for n in xrange(self.col)]

		for j in xrange(self.col):
			for i in xrange(self.row):
				transposed[i][j] = self.mat[j][i]

		return Matrix(transposed)

	def outer(self, b):
		'''b: Matrix object'''
		out = [[0 for n in xrange(b.row*b.col)] for m in xrange(self.row*self.col)]

		mat_flatten = [item for inner in self.mat for item in inner]
		b_flatten = [item for inner in b.mat for item in inner]

		for j in xrange(len(b_flatten)):
			for i in xrange(len(mat_flatten)):
				out[i][j] = mat_flatten[i] * b_flatten[j]

		return Matrix(out)

	def trace(self):
		if self.row != self.col:
			raise ValueError('shapes (%d,%d) not aligned' % (self.row, self.col))

		trace_a = sum([self.mat[i][i] for i in xrange(self.row)])

		return trace_a

	def identity(self, n):
		E = [[0 for j in xrange(n)] for i in xrange(n)]

		for i in xrange(n):
			E[i][i] = 1

		return Matrix(E)


	def multiply(self, b):
		'''b: Matrix object'''
		if self.row != b.row or self.col != b.col:
			raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (self.row, self.col, b.row, b.col))

		out = [[0 for n in xrange(self.col)] for m in xrange(self.row)]

		for j in xrange(self.col):
			for i in xrange(self.row):
				out[i][j] = self.mat[i][j] * b.mat[i][j]

		return Matrix(out)

	def direct_sum(self, b):
		'''b: Matrix object'''
		if self.row != b.row or self.col != b.col:
			raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (self.row, self.col, b.row, b.col))

		out = [[0 for n in xrange(self.col)] for m in xrange(self.row)]

		for j in xrange(self.col):
			for i in xrange(self.row):
				out[i][j] = self.mat[i][j] + b.mat[i][j]

		return Matrix(out)

	def get_shape(self):
		return [self.row, self.col]

	def get_row(self):
		return self.row

	def get_col(self):
		return self.col


# Function group
def dot(a, b):
	'''a, b: 2-D list'''
	if len(a[0]) != len(b):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	out = [[0 for n in xrange(len(b[0]))] for m in xrange(len(a))]

	for j in xrange(len(b[0])):
		for i in xrange(len(a)):
			for k in xrange(len(a[0])):
				out[i][j] += a[i][k]*b[k][j]

	return out


def transpose(a):
	'''a: 2-D list'''
	transposed = [[0 for m in xrange(len(a))] for n in xrange(len(a[0]))]

	for j in xrange(len(transposed[0])):
		for i in xrange(len(transposed)):
			transposed[i][j] = a[j][i]

	return transposed


def outer(a, b):
	'''a, b: 2-D list'''
	out = [[0 for n in xrange(len(b)*len(b[0]))] for m in xrange(len(a)*len(a[0]))]

	a_flatten = [item for inner in a for item in inner]
	b_flatten = [item for inner in b for item in inner]

	for j in xrange(len(b_flatten)):
		for i in xrange(len(a_flatten)):
			out[i][j] = a_flatten[i] * b_flatten[j]

	return out


def trace(a):
	if len(a) != len(a[0]):
		raise ValueError('shapes (%d,%d) not aligned' % (len(a), len(a[0])))

	return sum([a[i][i] for i in xrange(len(a))])


def identity(n):
	E = [[0 for j in xrange(n)] for i in xrange(n)]

	for i in xrange(n):
		E[i][i] = 1

	return E


def zeros(row, col):
	return [[0 for n in xrange(col)] for m in xrange(row)]


def multiply(a, b):
	'''a, b: 2-D list'''
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	out = [[0 for n in xrange(len(a[0]))] for m in xrange(len(a))]

	for j in xrange(len(a[0])):
		for i in xrange(len(a)):
			out[i][j] = a[i][j] * b[i][j]

	return out


def direct_sum(a, b):
	'''a, b: 2-D list'''
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	out = [[0 for n in xrange(len(a[0]))] for m in xrange(len(a))]

	for j in xrange(len(a[0])):
		for i in xrange(len(a)):
			out[i][j] = a[i][j] + b[i][j]

	return out
