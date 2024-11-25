class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        given = n
        productOfDigits = 1
        sumOfDigits = 0
        while(given):
            temp = given % 10
            productOfDigits *= temp
            sumOfDigits += temp
            given = given // 10
        return productOfDigits - sumOfDigits