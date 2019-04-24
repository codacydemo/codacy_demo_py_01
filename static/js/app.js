function hello() {
    return "Hello";
}
function world() {
    return "World";
}

function aVeryComplexMethod(isOk) {
    if (isOk) {
        if(true){
            for(i = 0; i < 10; i++){
                call(hello, function (sender) {
                    setTimeout(function () {
                        console.log(sender.caller);
                    }, 500);
                });
            }
        }
    }
}

function call(subject, callback) {
    alert(`Calling my ${subject}.`);
    callback({ caller: 'method' });
}
// Basic export
export { hello, world };