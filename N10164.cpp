# include<stdio.h>
# include<vector>
# include <iostream>
using namespace std;
vector<vector<int> > DP;
int getAns(int,int,int,int);
int main(){
    int n,m,k;
    scanf("%d %d %d",&n,&m,&k);
    DP.assign(n+1,vector<int>(m+1,-1));
    int km = k%m;
    if (km==0)
        km = m;
    int kn = (k/(m))+1;
    if (km == m)
        kn -= 1;
    DP[1][1] = 1;
    if (k != 0){
        getAns(1,1,kn,km);
        printf("%d",getAns(kn,km,n,m));
    }else{
        printf("%d",getAns(1,1,n,m));
    }
    return 0;
}
int getAns(int startN,int startM,int curN,int curM){
    if(curN == startN && curM == startM){
        return DP[curN][curM];
    }
    if(curN < startN || curM < startM){
        return 0;
    }
    if (DP[curN][curM] != -1)
        return DP[curN][curM];
    
    DP[curN][curM] = getAns(startN,startM,curN-1,curM) + getAns(startN,startM,curN,curM-1);
    return DP[curN][curM];
    
}
