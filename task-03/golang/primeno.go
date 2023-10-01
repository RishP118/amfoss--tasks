package main
import "fmt"

func Prime(n int) bool {
	if n <= 2 {
		return true
	} else if n%2 == 0 {
		return false
	}

	for i := 2; i*i <= n; i += 2 {
	    if n%i == 0 {
			return false
		}
	}

	return true
}

func printP(j int) {
	for i := 1; i <= j; i++ {
		if Prime(i) {
			fmt.Println(i)
		}
	}
}
func main() {
	var n int
	fmt.Print("Enter n: ")
	fmt.Scanln(&n)
	printP(n)
}
