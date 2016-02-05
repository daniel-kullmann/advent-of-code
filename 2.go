package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
)

func main() {
	content, err := ioutil.ReadFile("./2.txt")
	strContent := string(content)
	if err != nil {
		panic(err)
	}
	var area int64 = 0
	for _, line :=	range strings.Split(strContent, "\n") {
		if line == "" { break }
		strSizes := strings.Split(line, "x")
		sizes := make([]int64, 0)
		for _, strSize := range strSizes {
      size, _ := strconv.ParseInt(strSize, 10, 0)
      sizes = append(sizes, size)
		}
		sides := [3]int64{sizes[0]*sizes[1], sizes[1]*sizes[2], sizes[0]*sizes[2]}
		smallestSide := sides[0]
		for _, v := range sides {
			if v < smallestSide {
				smallestSide = v
			}
		}
		area += smallestSide + 2*(sides[0] + sides[1] + sides[2])
	}

	fmt.Println(area)

}
