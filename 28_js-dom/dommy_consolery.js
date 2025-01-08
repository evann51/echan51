// KungFuPandaSquad/2 :: Leon Huang, Evan Chan
// SoftDev pd5
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console == print
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x)
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree -- adds "text" to the numbered list
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree -- uses index
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red -- doesn't do anything to the items that are already blue (item 1-6)
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors -- doesn't do anything to the items that are already blue (item 1-6)
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
var fibo = function(n)
{
    if(n==0){
        return 0;
    }
    else if(n==1){
        return 1;
    }
    else return fibo(n-1)+fibo(n-2)
};
// FAC
var fact = function(n)
{
    if(n<0) {
        return 0;
    }
    else if(n==0) {
        return 1;
    }
    else {
        return n*fact(n-1)
    }
};
// GCD
var gcd = function(n,j) 
{
    if (j==0) {
        return n;
    }
    else {
        return gcd(j,n%j)
    }
};

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => { // const instead of var and no function before parameters
    // body
    return retVal;
};
const myFxn2 = (n) => {
    return n*2;
};