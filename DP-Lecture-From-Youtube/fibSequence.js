/*Write a function to find that takes in a number as an argument and return the n-th number in the fibonacci sequence

What is a fibonacci sequence: The first and second number in the sequence are 1. To generate the next number of the sequence, we sum the previous two. 

fib(n) = 1,1,2,3,5,8,13,21,34,...
*/ 

// implementation

const fib = (n) => {
	if(n <= 2){
		return 1;
	}

	return fib(n-1) + fib(n-2)
}



console.log(fib(6))
console.log(fib(7)) 
console.log(fib(8))
//taking too long for a regular recursion.
console.log(fib(50)) 
