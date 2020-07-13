/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        
        if(cloned->val==target->val) return cloned;
        TreeNode* result==NULL;//最好先初始化會比較好,遞迴的每一個{}裡面的TreeNode result都不會 是同一個值
        if(cloned->left){
            
            result = getTargetCopy(original, cloned->left, target); //return 回來的值要用result去接
        }
        if(!result){
            if(cloned->right){
            result = getTargetCopy(original, cloned->right, target);
            }
        }
        /*for(int i=0;i<100;i++){
            
        }
        cout<<i<<endl; //(測試用)變數一出{}就沒有用了*/ 
        return result;
    }
       
};
