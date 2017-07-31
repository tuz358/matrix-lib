#!/usr/bin/ruby

require("./mat")

def printmatrix(a)
  a.each_index do |i|
    a[0].each_index do |j|
      print a[i][j],"\t"
    end
    print "\n"
  end
  print "\n"
end

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,0,0],[0,1,0],[0,0,1]]

print "matrix a: \n"
printmatrix(a)
print "matrix b: \n"
printmatrix(b)

print "dot: \n"
c = dot(a,b)
printmatrix(c)

print "transpose: \n"
c = transpose(a)
printmatrix(c)

print "outer: \n"
c = outer(a, b)
printmatrix(c)

print "trace: "
c = trace(a)
print c,"\n"

print "identity: \n"
e = identity(3)
printmatrix(e)

print "multiply: \n"
c = multiply(a, b)
printmatrix(c)

print "direct_sum: \n"
c = direct_sum(a, b)
printmatrix(c)
