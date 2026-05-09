class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {

        List<int[]> tripletList = new ArrayList<>();

        
        for ( int i = 0; i < triplets.length; i++ ) {
            // Eliminate all triplets that contain an element triplet[x][i] > target[i]
            if ( triplets[i][0] > target[0] || triplets[i][1] > target[1] || triplets[i][2] > target[2]) continue;
            // Eliminate all triplets that do not have an element triplet[x][i] = target[i] as we cannot reach the target using this triplet
            if ( triplets[i][0] != target[0] && triplets[i][1] != target[1] && triplets[i][2] != target[2]) continue; 
            else tripletList.add(triplets[i]);
        }

        
        // for ( int[] triplet : tripletList ) {
        //     System.out.println("[" + triplet[0] + "," + triplet[1] + "," + triplet[2] + "]");
        // }

        if ( tripletList.isEmpty() ) return false;

        boolean flag1 = false;
        boolean flag2 = false;
        boolean flag3 = false;

        for ( int[] triplet : tripletList ) {
            if ( triplet[0] == target[0] ) flag1 = true;
            if ( triplet[1] == target[1] ) flag2 = true;
            if ( triplet[2] == target[2] ) flag3 = true;
        }

        if ( flag1 == true && flag2 == true && flag3 == true) return true;
        return false;
        
    }
}
