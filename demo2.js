const howSum = (targeSum, numbers) => {
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    for (let num of numbers){
        const remainder = targetSum -num;
        const remainderResult = howSum(remainder, numbers);
        if (remainderResult !== null){
            return [...remainderResult, num];
        }
    }
    return null;
};
console.log(howSum(7, [2,3]))
console.log(howSum([7, [5,4,3]]))
console.log(8, [2,3,5,4,6])
