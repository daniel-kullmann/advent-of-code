package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	content, err := ioutil.ReadFile("./3.txt")
	if err != nil {
		panic(err)
	}
	strContent := string(content)

	var counter map[string]int
	var x int64
	var y int64
	counter = make(map[string]int)
	x = 0
	y = 0
	counter[fmt.Sprintf("%d:%d", x, y)] += 1
	for _, char := range strContent {
		switch char {
		case '^':
			y -= 1
		case 'v':
			y += 1
		case '<':
			x -= 1
		case '>':
			x += 1
		default:
			fmt.Printf("Unknown character %c", char)
		}

		counter[fmt.Sprintf("%d:%d", x, y)] += 1

	}

	var count int

	for _, v := range counter {
		if v >= 1 {
			count += 1
		}
	}

	fmt.Println(count)

}
