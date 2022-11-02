const canSum = (targetSum, numbers, memo = {}) => {
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    for (let num of numbers) {
        const remainder = targetSum - num;
        if (canSum(remainder, numbers, memo) === true){
            return true;

        }
    }
    return false;
};
console.log(canSum(7,[2,3]));
console.log(canSum(7,[3,2,4, 7]));

