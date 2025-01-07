//Team KungFuPandaSquad/2 :: Evan Chan and Leon Huang
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

var fact = fac(n){
if(n<0){
    return 0;
  }
  else if(n==0){
    return 1;
  }
  else return n*fac(n-1);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)


//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

var fibo = fib(n){
if(n==0){
    return 0;
}
else if(n==1){
    return 1;
}
else return fib(n-1)+fib(n-2)
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

//=================================================================
