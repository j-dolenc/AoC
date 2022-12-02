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
            //roundSum+=1
            if(elf == "A"){
                roundSum+=3
            }
            else if(elf == "B"){
                roundSum+=1
            }
            else{
                roundSum+=2
            }
        }
        else if(me == "Y"){
            roundSum+=3
            if(elf == "A"){
                roundSum+=1
            }
            else if(elf == "B"){
                roundSum+=2
            }
            else{
                roundSum+=3
            }
        }
        else{
            roundSum+=6
            if(elf == "A"){
                roundSum+=2
            }
            else if(elf == "B"){
                roundSum+=3
            }
            else{
                roundSum+=1
            }
        }
        sum+=roundSum
    }
    console.log(sum)
})

