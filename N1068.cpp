# include<stdio.h>
# include<vector>
using namespace std;

vector<vector<int> > adjList;
int getAns(int,int,int);
int main(){
    int num,idx,root,del;
    scanf("%d",&num);
    adjList.assign(num,vector<int>());
    for(int i = 0; i< num;i++){
        scanf("%d",&idx);
        if (idx == -1){
            root = i;
            continue;
        }
        adjList[idx].push_back(i);
    }
    scanf("%d",&del);
    int result = getAns(del,root,root);
    printf("%d\n",result);
    return 0;
}
int getAns(int avoid,int parent,int root){
    if (parent == avoid)
        return 0;
    int size_child = adjList[parent].size();
    if (size_child == 0)
        return 1;
    
    int val = 1;
    if (parent == root)
        val = 0;
    int tag = 1;
    for (int i = 0;i<size_child;i++){
        int addVal = getAns(avoid,adjList[parent][i],root);
        if (addVal != 0 && tag && parent != root){
            val -= 1;
            tag = 0;
        }
        
        val += addVal;
    }
    return val;
}
