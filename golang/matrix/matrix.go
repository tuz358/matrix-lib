package matrix

func Dot(a [][]float32, b [][]float32) ([][]float32) {
	out := make([][]float32, len(b[0]))
	for i := range out {
		out[i] = make([]float32, len(a))
	}

	for j := 0 ; j < len(b) ; j++ {
		for i := 0 ; i < len(a) ; i++ {
			for k := 0 ; k < len(a[0]) ; k++ {
				out[i][j] += a[i][k]*b[k][j]
			}
		}
	}
	return out
}

func Transpose(a [][]float32) ([][]float32) {
	transposed := make([][]float32, len(a[0]))
	for i := range transposed {
		transposed[i] = make([]float32, len(a))
	}

	for j := 0; j < len(a[0]); j++ {
		for i := 0; i < len(a); i++ {
			transposed[i][j] = a[j][i]
		}
	}
	return transposed
}

func Inverse2d(a [][]float32) ([][]float32) {
	inversed := [][]float32{{0, 0}, {0, 0}}

	det_a := a[0][0] * a[1][1] - a[0][1] * a[1][0]

	inversed[0][0] =  a[1][1] / det_a
	inversed[0][1] = -a[0][1] / det_a
	inversed[1][0] = -a[1][0] / det_a
	inversed[1][1] =  a[0][0] / det_a

	return inversed
}

func Outer(a [][]float32, b [][]float32) ([][]float32) {
	out := make([][]float32, len(b)*len(b[0]))
	for i := range out {
		out[i] = make([]float32, len(a)*len(a[0]))
	}

	a_flatten := make([]float32, len(a)*len(a[0]))
	b_flatten := make([]float32, len(b)*len(b[0]))

	for i := 0; i < len(a_flatten); i++ {
		a_flatten[i] = a[int(i/len(a))][int(i%len(a[0]))]
	}
	for j := 0; j < len(b_flatten); j++ {
		b_flatten[j] = b[int(j/len(b))][int(j%len(b[0]))]
	}

	for j := 0; j < len(b_flatten); j++ {
		for i := 0; i < len(a_flatten); i++ {
			out[i][j] = a_flatten[i] * b_flatten[j]
		}
	}
	return out
}

func Trace(a [][]float32) (float32) {
	var trace_a float32 = 0
	for i := 0; i < len(a); i++ {
		trace_a += a[i][i]
	}
	return trace_a
}

func Identity(n int) ([][]float32) {
	E := make([][]float32, n)
	for i := range E {
		E[i] = make([]float32, n)
	}

	for i := 0; i < n; i++ {
		E[i][i] = 1
	}
	return E
}

func Multiply(a [][]float32, b [][]float32) ([][]float32) {
	out := make([][]float32, len(a[0]))
	for i := range out {
		out[i] = make([]float32, len(a))
	}

	for j := 0; j < len(a[0]); j++ {
		for i := 0; i < len(a); i++ {
			out[i][j] = a[i][j] * b[i][j]
		}
	}
	return out
}

func Direct_sum(a [][]float32, b [][]float32) ([][]float32) {
	out := make([][]float32, len(a[0]))
	for i := range out {
		out[i] = make([]float32, len(a))
	}

	for j := 0; j < len(a[0]); j++ {
		for i := 0; i < len(a); i++ {
			out[i][j] = a[i][j] + b[i][j]
		}
	}
	return out
}
