#include <stdio.h>
#include <vector>
# define DIV 10007
using namespace std;
vector<vector<int> > T2;
int main(){
    int n,k;
    scanf("%d %d",&n,&k);  
    T2.assign(k+1,vector<int>(n+1,0));
    for(int i = 0;i<k+1;i++){
        for(int j = i;j<n+1;j++){
            if (i ==0){
                T2[i][j] = 1;
                continue;
            }
            T2[i][j] = (T2[i-1][j-1]+T2[i][j-1])%DIV;

        }
    }
    printf("%d\n",T2[k][n]);
    return 0;
}
