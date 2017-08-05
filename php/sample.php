<?php
require('matrix.php');

$a = array(array(1, 2, 3), array(4, 5, 6), array(7, 8, 9));
$b = array(array(1, 0, 0), array(0, 1, 0), array(0, 0, 1));

$matrix = new Matrix($a);


function printmatrix($data) {
  for ($i = 0; $i < count($data); $i++) {
    for ($j = 0; $j < count($data[0]); $j++) {
      echo $data[$i][$j].' ';
    }
    echo "\n";
  }
  echo "\n";
}

echo "matrix a:\n";
printmatrix($a);
echo "matrix b:\n";
printmatrix($b);

echo "dot(a, b):\n";
$out = $matrix->dot($b);
printmatrix($out);

echo "transpose(a):\n";
printmatrix($matrix->transpose());

echo "outer(a, b):\n";
printmatrix($matrix->outer($b));

echo "trace(a): ";
print($matrix->trace());
echo "\n";

echo "identity(3):\n";
printmatrix($matrix->identity(3));

echo "multiply(a, b):\n";
printmatrix($matrix->multiply($b));

echo "direct_sum(a, b):\n";
printmatrix($matrix->direct_sum($b));

 ?>
