impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut zero_count = 0;
        let mut idx = 0;
        for i in 0..nums.len(){
            if nums[i] != 0 {
                nums[idx] = nums[i];
                idx += 1;
            }else {
                zero_count += 1;
            }
        }
        for j in (idx..nums.len()).rev(){
            nums[j] = 0;
        }
    }
}