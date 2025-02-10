impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let possible_res_array = [12,23,34,45,56,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,12456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789];
        let mut res : Vec<i32> = Vec::new();
        for &val in possible_res_array.iter(){
            if val > high {
                break;
            }
            if val >= low {
            res.push(val)
            }
        }
        res   
    }
}