package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	content, err := ioutil.ReadFile("./1.txt")
	if err != nil {
		panic(err)
	}
	up := 0
	down := 0

	for _, ch := range content {
		if ch == '(' {
			up += 1
		} else if ch == ')' {
			down += 1
		}
	}

	fmt.Println(up - down)
}
