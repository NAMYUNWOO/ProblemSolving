# include<stdio.h>
# include<vector>
using namespace std;
vector<int> coinVec;
vector<vector<int> >DP;
int getAns(int,int);
int main(){
    int testCase,num,coin,money,possibleCase;
    scanf("%d",&testCase);
    while(testCase--){
       scanf("%d",&num);
       coinVec.assign(num,0);
       for(int i = 0; i<num;i++){
           scanf("%d",&coin);
           coinVec[i] = coin;
       }
       scanf("%d",&money);
       DP.assign(num,vector<int>(money+1,-1));
       possibleCase = getAns(money,num-1);
       printf("%d\n",possibleCase);
       
    }
    return 0;
}

int getAns(int money,int coin){
    if (money < 0 || coin < 0)
        return 0;
    if (money == 0 && coin == 0)
        return 1;
    if (DP[coin][money] != -1)
        return DP[coin][money];

    DP[coin][money] = getAns(money,coin-1) + getAns(money - coinVec[coin], coin);
    return DP[coin][money];

}
