impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut idx = 1;

        for i in 1..nums.len(){
            if nums[i-1] != nums[i]{
                nums[idx] = nums[i];
                idx += 1;

            }
        }
        return idx as i32;
    }
}