const fs = require('fs')

var input = '';
fs.readFile('input.txt', (err, inputD) => {
    if (err) throw err;

    //console.log(inputD.toString());
    input = inputD.toString();
    const arr = input.split(/\r?\n/);
    var sum = 0;

    for(var i = 0; i <arr.length; i++){
        
    }
    console.log(sum)
    
})
