const fs = require('fs')

var input = '';
fs.readFile('input.txt', (err, inputD) => {
    if (err) throw err;

    //console.log(inputD.toString());
    input = inputD.toString();
    const arr = input.split(/\r?\n/);
    
    var sum = 0;
    for(var i = 0; i <arr.length; i++){
        var roundSum= 0;
        var me = arr[i][2]
        var elf = arr[i][0]
        //console.log(arr[i]);
        if(me == "X"){
            roundSum+=1
            if(elf == "A"){
                roundSum+=3
            }
            else if(elf == "B"){
                roundSum+=0
            }
            else{
                roundSum+=6
            }
        }
        else if(me == "Y"){
            roundSum+=2
            if(elf == "A"){
                roundSum+=6
            }
            else if(elf == "B"){
                roundSum+=3
            }
            else{
                roundSum+=0
            }
        }
        else{
            roundSum+=3
            if(elf == "A"){
                roundSum+=0
            }
            else if(elf == "B"){
                roundSum+=6
            }
            else{
                roundSum+=3
            }
        }
        sum+=roundSum
    }
    console.log(sum)
})

