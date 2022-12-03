const fs = require('fs')

var input = '';
fs.readFile('input.txt', (err, inputD) => {
    if (err) throw err;

    //console.log(inputD.toString());
    input = inputD.toString();
    const arr = input.split(/\r?\n/);
    var sum = 0;

    for(var i = 0; i <arr.length; i++){
        var len = arr[i].length
        var double = "";
        for(var j = 0; j < len/2; j++){
            var curr1 = arr[i][j];
            
            for(var k = len/2; k < len; k++){
                var curr2 = arr[i][k];
                if(curr2 == curr1){
                    double = curr2
                }
            }

        }
        var ascii = double.charCodeAt(0);
        if(ascii < 95){
            ascii -= 38
        }
        else{
            ascii-=96
        }
        sum+=ascii;
    }
    console.log(sum)
    
})

