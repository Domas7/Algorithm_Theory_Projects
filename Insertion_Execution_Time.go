package main

import (
	"fmt"
	"time"
	"math/rand"
)

func insertion_sort(A []int) int {
	steps := 0
	for i := 1; i < len(A); i++ {
		key := A[i]
		j := i - 1
		steps += 2
		for j >= 0 && A[j] > key {
			A[j+1] = A[j]
			j = j -1
			steps += 2
		}
		A[j+1] = key
		steps += 1
	}
	return steps
}

func randomArray(size int) []int {
	A := make([]int, size)
	for i := 0; i < size; i++ {
		A[i] = rand.Intn(100)
	}
	return A
}

func main() {

	input_size := []int{100, 1000, 5000, 20000, 50000, 100000}

	for _, size := range input_size {
		A := randomArray(size)
		start_time := time.Now()
		counting_steps := insertion_sort(A)
		stop_time := time.Since(start_time)
		fmt.Println("Size: ", size)
		fmt.Println("Number of steps: ", counting_steps)
		fmt.Println("Time: ", stop_time)
	}
}