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

	for pos, ch := range content {
		if ch == '(' {
			up += 1
		} else if ch == ')' {
			down += 1
		}
		if up - down < 0 {
			fmt.Println(pos)
			break
		}
	}

}
