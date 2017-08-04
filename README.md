# matrix-lib

Matrix library implemented in various languages.

## Java
Version: javac 1.8.0_121

**Tutorial**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/java/
$ javac Sample.java matrix.java
$ java Sample
```


## Python
Version: 2.7.13, 3.6.0

**Getting Started**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/python/
```

**Example**
```
>>> import matrix
>>> a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> b = matrix.identity(3)
>>> b
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> matrix.dot(a, b)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>
```


## Ruby
Version: 2.0.0p648

**Getting Started**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/ruby/
```

**Example**
```
$ ruby ./sample.rb
matrix a:
1	2	3
4	5	6
7	8	9

matrix b:
1	0	0
0	1	0
0	0	1

dot:
1	2	3
4	5	6
7	8	9
...
...
```

## Go
Version: 1.8.3

**Demo**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/golang/
$ go run ./sample.go
```

## Javascript
**Requirement**
- node.js

**Demo**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/Javascript/
$ node ./sample.js
```
