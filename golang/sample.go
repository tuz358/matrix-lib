package main

import (
  "fmt"
  "./matrix"
)

func main () {
  a := [][]float32{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
  b := [][]float32{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}

  fmt.Println("matrix a:")
  printmatrix(a)
  fmt.Println()

  fmt.Println("matrix b:")
  printmatrix(b)
  fmt.Println()

  fmt.Println("dot(a, b):")
  printmatrix(matrix.dot(a, b))
  fmt.Println()

  fmt.Println("transpose(a):")
  printmatrix(matrix.transpose(a))
  fmt.Println()

  fmt.Println("outer(a, b):")
  printmatrix(matrix.outer(a, b))
  fmt.Println()

  fmt.Println("trace(a):")
  fmt.Println(matrix.trace(a))
  fmt.Println()

  fmt.Println("identity(3):")
  printmatrix(matrix.identity(3))
  fmt.Println()

  fmt.Println("multiply(a, b):")
  printmatrix(matrix.multiply(a, b))
  fmt.Println()

  fmt.Println("direct_sum(a, b):")
  printmatrix(matrix.direct_sum(a, b))
  fmt.Println()
}

func printmatrix(mat [][]float32){
  for i := 0; i < len(mat); i++ {
    for j := 0; j < len(mat[0]); j++ {
      fmt.Printf("%v ", mat[i][j])
    }
    fmt.Println()
  }
  return
}
