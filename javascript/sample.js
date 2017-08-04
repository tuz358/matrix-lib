
var matrix = require('./matrix.js')

var a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
var b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];


function printmatrix(a) {
  for (var i = 0; i < a.length; i++) {
    for (var j = 0; j < a[0].length; j++) {
      process.stdout.write(a[i][j] + " ");
    }
    process.stdout.write("\n");
  }
  process.stdout.write("\n");
}


console.log("matrix a:")
printmatrix(a)
console.log("matrix b:")
printmatrix(b)

console.log("dot(a,b)")
printmatrix(matrix.dot(a,b))

console.log("transpose(a,b)")
printmatrix(matrix.transpose(a,b))

console.log("outer(a,b)")
printmatrix(matrix.outer(a,b))

console.log("trace(a)")
console.log(String(matrix.trace(a)))
console.log("\n")

console.log("identity(a,b)")
printmatrix(matrix.identity(3))

console.log("multiply(a,b)")
printmatrix(matrix.multiply(a,b))

console.log("direct_sum(a,b)")
printmatrix(matrix.direct_sum(a,b))
