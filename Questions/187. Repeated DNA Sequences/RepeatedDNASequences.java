/* 
Run Envrioment:
Java JDK 14

Time and Space Complexity:
Time: O(len(s))
Space: O(len(s))
Actual Time: 18 ms
Actual Space: 47.6 MB
*/

import java.util.*;

public class RepeatedDNASequences {
    public static List<String> findSequences(String s) {
        if (s.length() < 10) {
            return new ArrayList<String>();
        }

        Set<String> visited = new HashSet<String>();
        Set<String> result = new HashSet<String>();

        for (int i = 0; i < s.length() - 10 + 1; i++) {
            String temp = s.substring(i, i + 10);
            
            if (visited.contains(temp)){
                result.add(temp);
            }

            visited.add(temp);
        }

        return new ArrayList<String>(result);
    }

    public static void main(String[] args){
        System.out.println(RepeatedDNASequences.findSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
        System.out.println(RepeatedDNASequences.findSequences("AAAAAAAAAAAAA"));
    }
}