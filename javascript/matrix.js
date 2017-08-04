
function dot(a, b) {
  var out = [...Array(b[0].length)].map(() => Array(a.length).fill(0));
  for (var j = 0; j < b.length; j++) {
    for (var i = 0; i < a.length; i++) {
      for (var k = 0; k < a[0].length; k++) {
        out[i][j] += a[i][k]*b[k][j];
      }
    }
  }
  return out
}

function transpose(a) {
  var transposed = [...Array(a[0].length)].map(() => Array(a.length).fill(0));
  for (var j = 0; j < a[0].length; j++) {
    for (var i = 0; i < a.length; i++) {
      transposed[i][j] = a[j][i];
    }
  }
  return transposed;
}

function outer(a, b) {
  var out = [...Array(b.length*b[0].length)].map(() => Array(a.length*a[0].length).fill(0));
  var a_flatten = [].concat.apply([], a);
  var b_flatten = [].concat.apply([], b);

  for (var j = 0; j < b_flatten.length; j++) {
    for (var i = 0; i < a_flatten.length; i++) {
      out[i][j] = a_flatten[i] * b_flatten[j];
    }
  }
  return out;
}

function trace(a) {
  var trace_a = 0;
  for (var i = 0; i < a[0].length; i++) {
    trace_a += a[i][i];
  }
  return trace_a;
}

function identity(n) {
  var E = [...Array(n)].map(() => Array(n).fill(0));
  for (var i = 0; i < n; i++) {
    E[i][i] = 1;
  }
  return E;
}

function multiply(a, b) {
  var out = [...Array(a[0].length)].map(() => Array(a.length).fill(0));
  for (var j = 0; j < a[0].length; j++) {
    for (var i = 0; i < a.length; i++) {
      out[i][j] = a[i][j] * b[i][j];
    }
  }
  return out;
}

function direct_sum(a, b) {
  var out = [...Array(a[0].length)].map(() => Array(a.length).fill(0));
  for (var j = 0; j < a[0].length; j++) {
    for (var i = 0; i < a.length; i++) {
      out[i][j] = a[i][j] + b[i][j];
    }
  }
  return out;
}

exports.dot = dot
exports.transpose = transpose
exports.outer = outer
exports.trace = trace
exports.identity = identity
exports.multiply = multiply
exports.direct_sum = direct_sum
