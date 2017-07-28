#!/usr/bin/ruby


def dot(a, b)
  c = Array.new(a.length, 0).map{Array.new(b[0].length, 0)}

  b[0].each_index do |j|
    a.each_index do |i|
      a[0].each_index do |k|
        c[i][j] += a[i][k]*b[k][j]
      end
    end
  end

  return c
end

def transpose(a)
  '''
  transposed = Array.new(a.length, 0).map{Array.new(a[0].length, 0)}

  transposed[0].each_index do |j|
    transposed.each_index do |i|
      transposed[i][j] = a[j][i]
    end
  end

  return transposed
  '''
  return a.transpose
end

def outer(a, b)
    c = Array.new(a.length*a[0].length, 0).map{Array.new(b.length*b[0].length, 0)}

    b.flatten.each_index do |j|
      a.flatten.each_index do |i|
        c[i][j] = a.flatten[i] * b.flatten[j]
      end
    end

    return c
end

def trace(a)
  #trace_a = a.map{|i| a[i][i]}.inject(:+)
  trace_a = 0
  a.each_index do |i|
    trace_a += a[i][i]
  end
  return trace_a
end

def identity(n)
  e = Array.new(n, 0).map{Array.new(n, 0)}

  e.each_index do |i|
    e[i][i] = 1
  end

  return e
end

def multiply(a, b)
  c = Array.new(a.length, 0).map{Array.new(a[0].length, 0)}

  a[0].each_index do |j|
    a.each_index do |i|
      c[i][j] = a[i][j] * b[i][j]
    end
  end

  return c
end

def direct_sum(a, b)
  c = Array.new(a.length, 0).map{Array.new(a[0].length, 0)}

  a[0].each_index do |j|
    a.each_index do |i|
      c[i][j] = a[i][j] + b[i][j]
    end
  end

  return c
end
