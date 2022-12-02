import { readFile } from 'fs';

var input = '';
readFile('input.txt', (err, inputD) => {
    if (err) throw err;

    //console.log(inputD.toString());
    input = inputD.toString();
    const arr = input.split(/\r?\n/);
    
    // for(var i = 0; i <arr.length; i++){
        
    // }
    
})

