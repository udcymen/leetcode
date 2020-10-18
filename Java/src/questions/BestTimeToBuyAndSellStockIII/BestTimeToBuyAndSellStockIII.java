package questions.BestTimeToBuyAndSellStockIII;

public class BestTimeToBuyAndSellStockIII {
    public static int maxProfit(int[] prices) {

        int firstMinPrice = Integer.MAX_VALUE;
        int secondMinPrice = Integer.MAX_VALUE;
        int firstResult = 0;
        int secondResult = 0;

        for (int price : prices) {

            firstMinPrice = Math.min(firstMinPrice, price);
            firstResult = Math.max(firstResult, price - firstMinPrice);

            secondMinPrice = Math.min(secondMinPrice, price - firstResult);
            secondResult = Math.max(secondResult, price - secondMinPrice);
        }

        return secondResult;
    }

    public static void main(String[] args) {
        System.out.println(BestTimeToBuyAndSellStockIII.maxProfit(new int[] { 3, 3, 5, 0, 0, 3, 1, 4 }));
        System.out.println(BestTimeToBuyAndSellStockIII.maxProfit(new int[] { 1, 2, 3, 4, 5 }));
        System.out.println(BestTimeToBuyAndSellStockIII.maxProfit(new int[] { 7, 6, 4, 3, 1 }));
        System.out.println(BestTimeToBuyAndSellStockIII.maxProfit(new int[] { 1 }));
    }
}
