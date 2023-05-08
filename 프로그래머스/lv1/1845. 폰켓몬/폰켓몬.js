const solution = (nums) => {
    const set = new Set(nums);

    const temp = Array.from(set);
    
    let answer = temp.length;
    
    if (answer > nums.length / 2) answer = nums.length/2;
    
    return answer;
}