class Solution {
    public int[] countBits(int n) {
        
        int[] list = new int[n + 1];
        int[] res  = new int[n + 1];

        for ( int i = 0; i <=n; i++ ) {
            list[i] = i;
        }

        for (int num : list ) {
            int counter = 0;
            int index   = num;
            while ( num != 0 ) {
                if ( (num & 1) == 1 ) counter++;
                num >>= 1;
            }
            res[index] = counter;
        }
        return res;
    }
}
