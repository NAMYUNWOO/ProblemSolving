#include<stdio.h>
#include<stack> 
#include<algorithm>
#include<vector>
using namespace std;
vector<pair<long long,long long> > S;
vector<long long> A;
int main(){
    int n;
    long long left, maxArea,currentArea,top;
    while (true){
        maxArea = top = -1;
        scanf("%d",&n);
        if(n == 0)
            return 0;
        A.assign(n+1,0);
        S.assign(n+1,make_pair(0,0));
        for(int i = 0;i<=n;i++){
            if(i<n)
                scanf("%lld",&A[i]);
            while(top>= 0&& (i==n||S[top].first > A[i])){
                if(top>0)
                    left = S[top-1].second;
                else
                    left = -1;
                currentArea = (i-left-1)*S[top].first;
                --top;
                if(currentArea>maxArea)
                    maxArea = currentArea;
            }
            if(i<n){
                ++top;
                S[top].first = A[i];
                S[top].second = i;
            }
        }
        printf("%lld\n",maxArea);
    }
    return 0;
}
