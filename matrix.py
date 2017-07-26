#-*- coding: utf-8 -*-


def dot(a, b):
	if len(a[0]) != len(b):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	c = [[0 for n in xrange(len(b[0]))] for m in xrange(len(a))]

	for j in xrange(len(b[0])):
		for i in xrange(len(a)):
			for k in xrange(len(a[0])):
				c[i][j] += a[i][k]*b[k][j]

	return c


def transpose(a):
	transposed = [[0 for m in xrange(len(a))] for n in xrange(len(a[0]))]

	for j in xrange(len(transposed[0])):
		for i in xrange(len(transposed)):
			transposed[i][j] = a[j][i]

	return transposed


def outer(a, b):
	c = [[0 for n in xrange(len(b)*len(b[0]))] for m in xrange(len(a)*len(a[0]))]

	a_flatten = [item for inner in a for item in inner]
	b_flatten = [item for inner in b for item in inner]

	for j in xrange(len(b_flatten)):
		for i in xrange(len(a_flatten)):
			c[i][j] = a_flatten[i] * b_flatten[j]

	return c


def trace(a):
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	trace_a = sum([a[i][i] for i in xrange(len(a))])

	return trace_a


def identity(n):
	E = [[0 for j in xrange(n)] for i in xrange(n)]

	for i in xrange(n):
		E[i][i] = 1

	return E


def multiply(a, b):
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	c = [[0 for n in xrange(len(a[0]))] for m in xrange(len(a))]

	for j in xrange(len(a[0])):
		for i in xrange(len(a)):
			c[i][j] = a[i][j] * b[i][j]

	return c


def direct_sum(a, b):
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		raise ValueError('shapes (%d,%d) and (%d,%d) not aligned' % (len(a), len(a[0]), len(b), len(b[0])))

	c = [[0 for n in xrange(len(a[0]))] for m in xrange(len(a))]

	for j in xrange(len(a[0])):
		for i in xrange(len(a)):
			c[i][j] = a[i][j] + b[i][j]

	return c
