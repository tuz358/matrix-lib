//import com.tuz358.matrix;

class Test {
  public static void main(String args[]){
    float[][] a = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    float[][] b = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

    matrix A = new matrix(a);
    matrix B = new matrix(b);
    matrix C = new matrix(3, 3);

    System.out.println("C = dot(A, B)");
    System.out.println("------------------");
    C = A.dot(B);
    printmatrix(A, "A");
    printmatrix(B, "B");
    printmatrix(C, "C");
    System.out.println("------------------");

    System.out.println("A_t = transpose(A)");
    System.out.println("------------------");
    matrix A_t = A.transpose();
    printmatrix(A_t, "A_t");
    System.out.println("------------------");

    System.out.println("C = outer(A, B)");
    System.out.println("------------------");
    C = A.outer(B);
    printmatrix(C, "C");
    System.out.println("------------------");

    System.out.println("tr_A = trace(A)");
    System.out.println("------------------");
    float tr_A = A.trace();
    System.out.println(java.text.MessageFormat.format("tr_A: {0}\n", tr_A));
    System.out.println("------------------");

    System.out.println("E3 = identity(3)");
    System.out.println("------------------");
    matrix E3 = new matrix(3, 3).identity(3);
    printmatrix(E3, "E3");
    System.out.println("------------------");

    System.out.println("C = multiply(A, B)");
    System.out.println("------------------");
    C = A.multiply(B);
    printmatrix(C, "C");
    System.out.println("------------------");

    System.out.println("C = direct_sum(A, B)");
    System.out.println("------------------");
    C = A.direct_sum(B);
    printmatrix(C, "C");
    System.out.println("------------------");
  }

  private static void printmatrix(matrix x, String name){
    System.out.println("matrix " + name + ":");
    for (int i = 0;i < x.data.length;i++) {
      for (int j = 0;j < x.data[0].length;j++) {
        System.out.print(String.valueOf(x.data[i][j]) + '\t');
      }
      System.out.println();
    }
    System.out.println();
  }

}
