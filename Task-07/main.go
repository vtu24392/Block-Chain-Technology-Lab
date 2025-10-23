package main

import (
"fmt"
"example.com/gopackage/reverse"
)

funcmain() {
input := "Golang"
output := reverse.ReverseString(input)
fmt.Println("Original String:", input)
fmt.Println("Reversed String:", output)
}
