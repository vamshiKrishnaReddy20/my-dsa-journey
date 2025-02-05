impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) { 
        for left_index in (0..(s.len() / 2)){
          let mut right_index = s.len()-1-left_index;
          s.swap(left_index,right_index);
        }
    }
}