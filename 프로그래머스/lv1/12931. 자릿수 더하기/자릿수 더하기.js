// // 예전 답
// const solution = (n) =>
// {
//     let answer = 0;
//     let temp = String(n);
    
//     const a = temp.split("");

//     for(let i = 0; typeof a[i] != 'undefined'; i++) {
//         answer += Number(a[i]);
//     }
    
//     return answer;
// }

// // 답 2
// const solution = (n) => n.toString().split('').reduce((acc, cur, i) => acc+=Number(cur),0)

const solution = (n) => Array.from(String(n), Number).reduce((acc, cur, i) => acc+=Number(cur),0)