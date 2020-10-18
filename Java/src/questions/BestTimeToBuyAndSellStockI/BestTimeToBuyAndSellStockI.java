public class BestTimeToBuyAndSellStockI {
    public static int maxProfit(int[] prices) {
        int result = 0;
        int minPrice = Integer.MAX_VALUE;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price > minPrice) {
                result = Math.max(result, price - minPrice);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(BestTimeToBuyAndSellStockI.maxProfit(new int[] { 7, 1, 5, 3, 6, 4 }));
        System.out.println(BestTimeToBuyAndSellStockI.maxProfit(new int[] { 7, 6, 4, 3, 1 }));
    }
}
