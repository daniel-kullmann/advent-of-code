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
	var ribbon int64 = 0
	for _, line :=	range strings.Split(strContent, "\n") {
		if line == "" { break }
		strSizes := strings.Split(line, "x")
		sizes := make([]int64, 0)
		for _, strSize := range strSizes {
      size, _ := strconv.ParseInt(strSize, 10, 0)
      sizes = append(sizes, size)
		}
		volume := sizes[0]*sizes[1]*sizes[2]

		largestLength := sizes[0]
		for _, v := range sizes {
			if v > largestLength {
				largestLength = v
			}
		}
		ribbon += volume + 2*(sizes[0] + sizes[1] + sizes[2] - largestLength)
	}

	fmt.Println(ribbon)

}
