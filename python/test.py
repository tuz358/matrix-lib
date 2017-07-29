#!/usr/bin/python
#-*- coding: utf-8 -*-

import matrix


def printmatrix(mat):
	for i in xrange(len(mat)):
		for j in xrange(len(mat[0])):
			print str(mat[i][j]) + ' ',
		print ''
	print ''

def main():
	a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	# b = matrix.identity(3)
	b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

	print 'matrix a: '
	printmatrix(a)
	print 'matrix b: '
	printmatrix(b)

	print '-'*10

	print 'dot(a, b) : '
	printmatrix(matrix.dot(a, b))

	print 'transpose(a) : '
	printmatrix(matrix.transpose(a))

	print 'outer(a, b) : '
	printmatrix(matrix.outer(a, b))

	print 'trace(a) : ' + str(matrix.trace(a)) + '\n'

	print 'identity(3) : '
	printmatrix(matrix.identity(3))

	print 'multiply(a, b) : '
	printmatrix(matrix.multiply(a, b))

	print 'direct_sum(a, b) : '
	printmatrix(matrix.direct_sum(a, b))

if __name__=='__main__':
	main()
