public class Solution {
    public int MaxProfit(int[] prices) {
        int buy = 0;
        int sell = 1;
        int max_profit = 0;
        int profit;
        
        while (sell < prices.Length){
            profit = prices[sell] - prices[buy];
                
            if (profit < 0){
                buy = sell;
            }
            
            max_profit = Math.Max(max_profit, profit);     
            sell++;
        }
        return max_profit;
    }
}