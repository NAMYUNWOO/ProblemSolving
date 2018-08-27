# include<stdio.h>
# include<queue>
# include<algorithm>

using namespace std;
typedef pair<int,int> P;
struct Order
{
    bool operator()(pair<int,int> const& a, pair<int,int> const& b) const
    {
        return a.first > b.first;
    }
};
queue<pair<int,int> > Q;
priority_queue<pair<int,int>,vector<pair<int,int>>,Order> PQ;

int main(){
    int n,s,num;
    int idx2Out;
    scanf("%d %d",&n,&s);
    for (int i = 0;i<n;i++){
        if(Q.size() == s){
            idx2Out = Q.front().second;
            Q.pop();
            while(idx2Out >= PQ.top().second){
                PQ.pop();
            }
        }
        scanf("%d",&num);
        Q.push(make_pair(num,i));
        PQ.push(make_pair(num,i));
        if (i != n-1 )
            printf("%d ",PQ.top().first);
        else
            printf("%d",PQ.top().first);

    }

    return 0;
}
