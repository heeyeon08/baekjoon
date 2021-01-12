// 백준 9012번: 괄호

'use strict';

class Stack{
    constructor(){
        this.store = [];
    }

    push(item){
        this.store.push(item);
    }

    pop() {
        return this.store.pop();
    }

    isEmpty() {
        if (this.store.length == 0)
            return true;
        else return false;
    }
}

const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

function ParenCheck(tmp){
    const stack = new Stack();
    let item, pre;

    for (let i = 0; i < tmp.length; ++i){
        
        item = tmp[i]
        
        if (item == '(') stack.push(item);
        
        else if (item == ')'){

            if (stack.isEmpty()) return false; // 조건 2
            
            pre = stack.pop();

            if (item == ')' && pre != '(')
                return false; // 조건 3
        }
    }
    if (!stack.isEmpty()) return false; // 조건 1
    
    return true;
}

{
    let tmp;

    for (let i = 1; i < Number(input[0]) + 1; ++i){

        tmp = input[i];

        if (ParenCheck(tmp))
            console.log('YES');

        else console.log('NO');
    }
}
