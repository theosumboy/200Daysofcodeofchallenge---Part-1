class Solution {
    static int max=-1;
    
    public static int findMaxForN(Node root, int n) {
       
        traverse(root,n);
        int ans = max;
        max = -1;
        return ans;
    }
    public static void traverse(Node root,int n){
         if(root==null)
            return;
            
        traverse(root.left,n);
        if(root.key>max&&root.key<=n){
            max = root.key;
        }
        traverse(root.right,n);
        
    }
}
