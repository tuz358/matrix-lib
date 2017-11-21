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

  fmt.Println("Dot(a, b):")
  printmatrix(matrix.Dot(a, b))
  fmt.Println()

  fmt.Println("Transpose(a):")
  printmatrix(matrix.Transpose(a))
  fmt.Println()

  fmt.Println("Inverse2d([][]float32{{1, 2}, {3, 4}}):")
  inversed, err := matrix.Inverse2d([][]float32{{1, 2}, {3, 4}})
  if err != nil {
    fmt.Println(err)
  } else {
    printmatrix(inversed)
  }
  fmt.Println()

  fmt.Println("Outer(a, b):")
  printmatrix(matrix.Outer(a, b))
  fmt.Println()

  fmt.Println("Trace(a):")
  fmt.Println(matrix.Trace(a))
  fmt.Println()

  fmt.Println("Identity(3):")
  printmatrix(matrix.Identity(3))
  fmt.Println()

  fmt.Println("Multiply(a, b):")
  printmatrix(matrix.Multiply(a, b))
  fmt.Println()

  fmt.Println("Direct_sum(a, b):")
  printmatrix(matrix.Direct_sum(a, b))
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
