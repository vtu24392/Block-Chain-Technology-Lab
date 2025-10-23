package reverse

// ReverseString reverses a given string
funcReverseString(s string)string {
result :=""
for _, v := range s {
result = string(v) + result
    }
return result
}
