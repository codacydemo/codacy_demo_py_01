function hello() {
    let a = "dummy"
    let newline = ""
    let newline2 = ""
    return "Hello";
}


function world() {
    let a = "dummy"
    let newline = ""
    let newline2 = ""
    let b = "line"
    return "World";
}

function complex(isOk, totalItems) {
    let result = 0
    if(isOk){
        for(let i = 0; i < totalItems; i++){
            let j = 0;
            while(j < 10){
                if(j % 2 == 0){
                    result += j*i;
                    if(result % 10 == 0){
                        world();
                    }
                }
                j++;
            }
        }
    }
}