
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        
        //add to a hash set
        // if element is in hash set:
                //get max_length then delete hash set from the beginning till that element
        
        use std::collections::HashSet;
        
        let mut char_set: HashSet<char> = HashSet::new();
        let mut ptr = 0usize;
        let mut char_ptr = 0usize;
        let mut max_length = 0usize;
        let chars: Vec<char> = s.chars().collect();
        
        while ptr < s.len() {     
            while char_set.contains(&chars[ptr]) {
                max_length = max_length.max(char_set.len());
                char_set.remove(&chars[char_ptr]);
                char_ptr += 1;
            }
            char_set.insert(chars[ptr]);
            ptr += 1;
        }
        max_length.max(char_set.len()) as i32
    }
}

/*
    time: O(n*k)
    space: O(n)
*/