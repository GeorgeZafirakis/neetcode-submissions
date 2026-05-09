class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = getMax(piles);

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (canFinish(piles, h, mid)) {
                r = mid - 1; // Try a smaller speed
            } else {
                l = mid + 1; // Increase speed
            }
        }
        return l; // The minimum valid eating speed
    }

    private int getMax(int[] piles) {
        int max = 0;
        for (int pile : piles) {
            max = Math.max(max, pile);
        }
        return max;
    }

    private boolean canFinish(int[] piles, int h, int k) {
        int hours = 0;
        for (int pile : piles) {
            hours += (pile + k - 1) / k; // Equivalent to Math.ceil(pile / k)
        }
        return hours <= h;
    }
}