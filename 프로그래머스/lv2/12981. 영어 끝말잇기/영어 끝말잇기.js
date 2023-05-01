// 틀린 사람의 [번호, 차례] 를 리턴

const solution = (n, words) => {
    let lastChar = ''; // words[i][words[i].length - 1]
    let circle = 0; // parseInt(index+1 / n) + 1
    let person = 0; // parseInt((index + 1) % n)
    
    const used = [words[0]];

    for (let i = 1; i < words.length; i++) {
        lastChar = words[i-1][words[i-1].length - 1]
        // 앞 단어의 마지막 문자와 뒤 단어의 첫 번째 문자가 같은지 확인
        if (words[i][0]  !== lastChar) {
            circle = parseInt(i / n) + 1
            person = parseInt(i % n + 1)
            
            return [person, circle]
        }
        // 중복된 단어 확인
        for (const w of used) {
            if (w === words[i]) {
                circle = parseInt(i / n) + 1
                person = parseInt(i % n + 1)
                console.log(used)
                console.log(`person : ${person} , circle : ${circle}`)
                return [person, circle]
            }
        }
        used.push(words[i])
    }
    
    return [0, 0]
}