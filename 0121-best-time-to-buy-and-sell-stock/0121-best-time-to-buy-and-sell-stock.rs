use std::cmp::max;
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut maxi = 0;
        for val in (0..prices.len()).rev(){
            if prices[val] > maxi{
                maxi = prices[val];
            }else{
                max_profit = max((maxi - prices[val]), max_profit);
            }
        }
        max_profit
        
    }
}