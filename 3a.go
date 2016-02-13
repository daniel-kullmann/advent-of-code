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
	var x, rx, y, ry int64
	counter = make(map[string]int)
	x = 0
	y = 0
	rx = 0
	ry = 0
	robo := true
	counter[fmt.Sprintf("%d:%d", x, y)] += 1
	for _, char := range strContent {
		if robo {
			switch char {
			case '^':
				ry -= 1
			case 'v':
				ry += 1
			case '<':
				rx -= 1
			case '>':
				rx += 1
			default:
				fmt.Printf("unknown character: %c", char)
			}

			counter[fmt.Sprintf("%d:%d", rx, ry)] += 1
		} else {
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
				fmt.Printf("unknown character: %c", char)
			}

			counter[fmt.Sprintf("%d:%d", x, y)] += 1
		}
		robo = !robo

	}

	var count int

	for _, v := range counter {
		if v >= 1 {
			count += 1
		}
	}

	fmt.Println(count)

}
