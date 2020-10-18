import utilities.java.TreeNode;

public class sumRootToLeaf {

    /* Attempt 1
    private void dfs(TreeNode root, String path, List<String> results) {
        path += String.valueOf(root.val);

        if (root.left == null && root.right == null){
            results.add((path));
        }
        else{
            if (root.left != null){
                dfs(root.left, path, results);
            }
            if (root.right != null){
                dfs(root.right, path, results);
            }
        }
    }

    public int sumRootToLeaf(TreeNode root) {
        int result = 0;

        if (root == null){
            return result;
        }

        List<String> results = new ArrayList<String>();
        dfs(root, "", results);

        for(String s : results){
            result += Integer.parseInt(s, 2);
        }

        return result;
    }
     */

    // Faster Solution
    private int dfs(TreeNode root, int result){
        if (root == null){
            return 0;
        }

        result = result * 2 + root.val;

        if (root.left == null && root.right == null){
            return result;
        }
        else{
            return dfs(root.left, result) + dfs(root.right, result);
        }
    }

    public static int sumofRootToLeafBinaryNumbers(TreeNode root){
        return dfs(root, 0);
    }

    public static void main(String args[]) {
        TreeNode root = new TreeNode(1);
        TreeNode left = new TreeNode(0);
        TreeNode right = new TreeNode(1);
        root.left = left;
        root.right = right;
        left.left = new TreeNode(0);
        left.right = new TreeNode(1);
        right.left = new TreeNode(0);
        right.right = new TreeNode(1);

        System.out.println(sumRootToLeaf.sumofRootToLeafBinaryNumbers(root));
    }
}
