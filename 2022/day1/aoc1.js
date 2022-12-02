const fs = require('fs')

var input = '';
fs.readFile('input.txt', (err, inputD) => {
    if (err) throw err;

    //console.log(inputD.toString());
    input = inputD.toString();
    const arr = input.split(/\r?\n/);
    
    var max1 = 0;
    var max2 = 0;
    var max3 = 0;

    var curr = 0;
    for(var i = 0; i < arr.length; i++){
        //console.log(arr[i])
        if(arr[i] != ""){
            curr = curr + parseInt(arr[i])
        }
        if(arr[i] == ""){
            if(curr > max1){
                max3 =max2
                max2 = max1
                max1 = curr

            }
            else if(curr > max2){
                max3 =max2
                max2 = curr
            }
            else if(curr > max3){
                max3 = curr
            }
            curr = 0
        }
        
    }
    console.log(curr)
    console.log(max1+max2+max3)
})

