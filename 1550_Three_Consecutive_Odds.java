class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int Consecutive_odds = 0;
        for (int i=0 ;i<arr.length;i++){
            if (arr[i] % 2 != 0){
                ++Consecutive_odds;
            }
            if (Consecutive_odds == 3){
                return true;
            }
            else if (arr[i]%2==0){
                Consecutive_odds = 0 ;
            }

        }
        return false;
    }
}