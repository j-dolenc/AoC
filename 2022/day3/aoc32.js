const fs = require('fs')

var input = '';
fs.readFile('input.txt', (err, inputD) => {
    if (err) throw err;

    //console.log(inputD.toString());
    input = inputD.toString();
    const arr = input.split(/\r?\n/);
    var sum = 0;
    for(var i = 0; i <arr.length; i+=3){
        var len = arr[i].length
        var double = "";
        
        for(var j = 0; j< len; j++){
        
            var curr1 = arr[i][j]

            for(var k = 0; k < arr[i+1].length;k++){

                var curr2 = arr[i+1][k]

                if(curr1 == curr2){

                    for(var l = 0; l < arr[i+2].length; l++){

                        var curr3 = arr[i+2][l]

                        if(curr2 == curr3){
                            double = curr3
                            console.log(double)
                            break;
                        }
                    }
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

