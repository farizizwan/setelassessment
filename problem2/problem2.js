var ary = [[[[[0]], [1]], [[[2], [3]]], [[4], [5]]]]
console.log(flatten(ary)); 

//function to flatten the array
function flatten(ary) {
    var ret = [];
    for(var i = 0; i < ary.length; i++) {
        if(Array.isArray(ary[i])) {
            ret = ret.concat(flatten(ary[i]));
        } else {
            ret.push(ary[i]);
        }
    }
    return ret;
}