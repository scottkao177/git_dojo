var num1 = 2
var num2 = 4

function add() {
    alert(num1 + num2)
    console.log("The answer is: ", num1 + num2)   
}

console.log(declaring)

function ifLoop() {
    for (var i = 0; 5; i++) {
        if (i % 2 == 0) {
            alert("True")
            console.log("Even")
        } else {
            alert("False")
            console.log("Odd")
        }
        console.log("The current value of i is: ", i)
    }
}

function ifLoop2() {
    for (var i = 0; <= 5; i++) {
        if (i % 2 == 0) {
            alert("True")
            console.log("Even")
        } else {
            alert("False")
            console.log("Odd")
        }
        console.log("The current value of i is: ", i)
    }
}

function ifLoop3() {
    for (var i = 0; <= 15; i++) {
        if (i % 2 == 0) {
            alert("True")
            console.log("Even")
            i=i+2
        } else {
            alert("False")
            console.log("Odd")
        }
        console.log("The current value of i is: ", i)
    }
}