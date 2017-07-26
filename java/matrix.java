//package com.tuz358;

public class matrix {
  float data[][];
  private int row, col;

  //matrix(){}

  matrix(int row, int col){
    if ((row < 0) || (col < 0)) {
      throw new IllegalArgumentException(java.text.MessageFormat.format("row and col must be greater than 0 or equal to 0: row={0}, col={1}", row, col));
    }

    this.data = new float[row][col];
    this.row = row;
    this.col = col;
  }

  matrix(float[][] data){
    this.row = data.length;
    this.col = data[0].length;
    this.data = data;
  }

  public float[][] dot(float x[][]){
    if (col != x.length) {
      throw new IllegalArgumentException(java.text.MessageFormat.format("shapes ({0},{1}) and ({2},{3}) not aligned", row, col, x.length, x[0].length));
    }

    float[][] c = new float[row][x[0].length];

    for (int j = 0;j < x[0].length;j++) {
      for (int i = 0;i < row;i++) {
        for (int k = 0;k < col;k++) {
          c[i][j] += data[i][k]*x[k][j];
        }
      }
    }

    return c;
  }

  public matrix dot(matrix x){
    float[][] c = this.dot(x.data);
    matrix ret = new matrix(c);
    return ret;
  }

  public float[][] T(){
    if (data == null) {
      throw new IllegalArgumentException("matrix data is null.");
    }

    float[][] transposed = new float[row][col];

    for (int j = 0;j < col;j++) {
      for (int i = 0;i < row;i++) {
        transposed[i][j] = data[j][i];
      }
    }

    return transposed;
  }

  public matrix transpose(){
    float[][] transposed = this.T();
    matrix ret = new matrix(transposed);
    return ret;
  }

  public float[][] outer(float x[][]){
    if (data == null) {
      throw new IllegalArgumentException("matrix data is null.");
    }

    float[][] c = new float[row*col][x.length*x[0].length];
    float[] data_flatten = new float[row*col];
    float[] x_flatten = new float[x.length*x[0].length];

    for (int i = 0;i < data_flatten.length;i++) {
      data_flatten[i] = data[(int)(i/row)][i%col];
    }
    for (int i = 0;i < x_flatten.length;i++) {
      x_flatten[i] = x[(int)(i/x.length)][i%x[0].length];
    }

    for (int j = 0;j < x_flatten.length;j++) {
      for (int i = 0;i < data_flatten.length;i++) {
        c[i][j] = data_flatten[i] * x_flatten[j];
      }
    }

    return c;
  }

  public matrix outer(matrix x){
    float[][] c = this.outer(x.data);
    matrix ret = new matrix(c);
    return ret;
  }

  public float trace(){
    if (row != col) {
      throw new IllegalArgumentException(java.text.MessageFormat.format("shapes ({0},{1}) not aligned", row, col));
    }

    float trace = 0f;
    for (int i = 0;i < row;i++) {
      trace += data[i][i];
    }

    return trace;
  }

  public matrix identity(int n){
    if (n < 1) {
      throw new IllegalArgumentException(java.text.MessageFormat.format("n should be natural number: n={0}",n));
    }

    float[][] E = new float[n][n];

    for (int j = 0;j < n;j++) {
      for (int i = 0;i < n;i++) {
        E[i][j] = i == j? 1 : 0;
      }
    }

    matrix ret = new matrix(E);

    return ret;
  }

  public float[][] multiply(float x[][]){
    if ((row != x.length) || (col != x[0].length)) {
      throw new IllegalArgumentException(java.text.MessageFormat.format("shapes ({0},{1}) and ({2},{3}) not aligned", row, col, x.length, x[0].length));
    }

    float[][] c = new float[row][col];

    for (int j = 0;j < col;j++) {
      for (int i = 0;i < row;i++) {
        c[i][j] = data[i][j] * x[i][j];
      }
    }

    return c;
  }

  public matrix multiply(matrix x){
    float[][] c = this.multiply(x.data);
    matrix ret = new matrix(c);
    return ret;
  }

  public float[][] direct_sum(float x[][]){
    if ((row != x.length) || (col != x[0].length)) {
      throw new IllegalArgumentException(java.text.MessageFormat.format("shapes ({0},{1}) and ({2},{3}) not aligned", row, col, x.length, x[0].length));
    }

    float[][] c = new float[row][col];

    for (int j = 0;j < col;j++) {
      for (int i = 0;i < row;i++) {
        c[i][j] = data[i][j] + x[i][j];
      }
    }

    return c;
  }

  public matrix direct_sum(matrix x){
    float[][] c = this.direct_sum(x.data);
    matrix ret = new matrix(c);
    return ret;
  }

}
