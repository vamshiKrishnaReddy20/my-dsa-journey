impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut left = 0;
        // println!("{}",nums[left]);
        for n in 0..nums.len(){
            if nums[n] != val{
                nums[left] = nums[n];
                left += 1;
            }
        }
        left as i32
         
    }
}