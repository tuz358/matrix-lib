# matrix-lib

Matrix library implemented in various languages.

## Java
OS: macOS 10.12.6  
Version: javac 1.8.0_121

**Tutorial**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/java/
$ javac Test.java matrix.java
$ java Test
```


## Python
OS: macOS 10.12.6  
Version: Python2.7.13, 3.6.0

**Getting Started**
```
$ git clone http://github.com/tuz358/matrix-lib
$ cd ./matrix-lib-master/python/
```

**Example**
```python
>>> import matrix
>>> a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> b = matrix.identity(3)
>>> b
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> matrix.dot(a, b)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>
```
