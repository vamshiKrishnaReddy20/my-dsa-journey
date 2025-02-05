impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut array = vec![];
        for i in (0..s.len()).rev(){
            array.push(s[i]);
           
        }
        for i in (0..s.len()){
            s[i] = array[i];
        }
    }
}