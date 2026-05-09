class Solution {
    public int getSum(int a, int b) {

        int carry = 0;
        int res   = 0;
        
        for ( int i = 0; i < 32; i++ ) {
            int a_bit   = (a >> i) & 1;
            int b_bit   = (b >> i) & 1;
            int cur_bit = a_bit ^ b_bit ^ carry;
            // This line can be replaced by 8 if statements (e.g. if ( a == 0 && b == 0 & c == 0) carry = 0)
            carry = (a_bit + b_bit + carry) >= 2 ? 1 : 0;
            if (cur_bit != 0) {
                res |= ( 1 << i );
            }
        }

        return res;
    }
}
