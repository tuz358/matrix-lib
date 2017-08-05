<?php
/**
 *
 */
class Matrix {
  public $data;
  public $row;
  public $col;

  function __construct($data) {
    $this->data = $data;
    $this->row = count($data);
    $this->col = count($data[0]);
  }

  function dot($b) {
    $out = array_fill(0, $this->row, array_fill(0, count($b[0]), 0));
    for ($j = 0; $j < count($b); $j++) {
      for ($i = 0; $i < $this->row; $i++) {
        for ($k = 0; $k < $this->col; $k++) {
          $out[$i][$j] += $this->data[$i][$k]*$b[$k][$j];
        }
      }
    }
    return $out;
  }

  function transpose() {
    $transposed = array_fill(0, $this->row, array_fill(0, $this->col, 0));
    for ($j = 0; $j < $this->col; $j++) {
      for ($i = 0; $i < $this->row; $i++) {
        $transposed[$i][$j] = $this->data[$j][$i];
      }
    }
    return $transposed;
  }

  function outer($b) {
    $out = array_fill(0, $this->row*$this->col, array_fill(0, count($b)*count($b[0]), 0));
    $data_flatten = array();
    array_walk_recursive($this->data, function($a) use (&$a_flatten) { $a_flatten[] = $a; });
    $b_flatten = array();
    array_walk_recursive($b, function($a) use (&$b_flatten) { $b_flatten[] = $a; });

    for ($j = 0; $j < count($b_flatten); $j++) {
      for ($i = 0; $i < count($a_flatten); $i++) {
        $out[$i][$j] = $a_flatten[$i] * $b_flatten[$j];
      }
    }
    return $out;
  }

  function trace() {
    $trace = 0;
    for ($i = 0; $i < $this->col; $i++) {
      $trace += $this->data[$i][$i];
    }
    return $trace;
  }

  function identity($n) {
    $E = array_fill(0, $n, array_fill(0, $n, 0));
    for ($i = 0; $i < $n; $i++) {
      $E[$i][$i] = 1;
    }
    return $E;
  }

  function multiply($b) {
    $out = array_fill(0, $this->row, array_fill(0, $this->col, 0));
    for ($j = 0; $j < $this->col; $j++) {
      for ($i=0; $i < $this->row; $i++) {
        $out[$i][$j] = $this->data[$i][$j] * $b[$i][$j];
      }
    }
    return $out;
  }

  function direct_sum($b) {
    $out = array_fill(0, $this->row, array_fill(0, $this->col, 0));
    for ($j = 0; $j < $this->col; $j++) {
      for ($i=0; $i < $this->row; $i++) {
        $out[$i][$j] = $this->data[$i][$j] + $b[$i][$j];
      }
    }
    return $out;
  }
}
?>
