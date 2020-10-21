package questions.SearchA2DMatrix;

import java.util.*;

public class SearchA2DMatrix {

    public static boolean searchMatrix(int[][] matrix, int target) {
        
        if (matrix.length == 0 || matrix[0].length == 0){
            return false;
        }
    
        int i = matrix[0].length - 1, j = 0;
        
        while (i > -1 && j < matrix.length){
            if (matrix[j][i] ==  target){
                return true;
            }
            else if (matrix[j][i] >  target){
                i--;
            }
            else{
                j++;
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        System.out.println(SearchA2DMatrix
                .searchMatrix(new int[][] { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 50 } }, 3));
        System.out.println(SearchA2DMatrix
                .searchMatrix(new int[][] { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 50 } }, 13));
        System.out.println(SearchA2DMatrix.searchMatrix(new int[][] {}, 0));
    }

}
