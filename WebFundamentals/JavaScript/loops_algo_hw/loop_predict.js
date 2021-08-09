// Prediction: 0 to 14 because <10, increments of 1 //
for (var num = 0; num < 15; num++){
    console.log(num);
}

// Prediction: 3 & 9 because <10, increments of 2 starting from 1, var i divided by 3 remainder equals 0 //
for (var i = 1; i < 10; i += 2) {
    if (i % 3 == 0) {
        console.log(i);
    }
}

// Prediction: 1, 4, 5, 8, 10, 11, 14, 16 because <=15, increments of 1, meets one of the conditions//
// (First condition) if var j divided by 2 remainder equals 0, increments of 2 //
// (second condition in case var j does not meet first condition) var j divided by 3 = 0, increments of 1 //

for(var j = 1; j <= 15; j++){  
    if(j % 2 == 0){                       
        j+=2;
    }
    else if(j % 3 == 0){                  
        j++;                                   
    }
    console.log(j);
}

