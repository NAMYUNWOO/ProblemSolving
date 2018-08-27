#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int isInCard(int,int *,int,int);
int main(){
    int n ;
    scanf("%d",&n);
    int *myCard = (int *)malloc(sizeof(int)*n);
    for(int i = 0;i<n;i++)
        scanf("%d",&myCard[i]);
    int k;
    scanf("%d",&k);
    int *card = (int *)malloc(sizeof(int)*k);
    for(int i = 0; i<k;i++)
        scanf("%d",&card[i]);
    sort(card,card+k);
    for(int i = 0;i<n;i++){
        printf("%d ",isInCard(myCard[i],card,0,n-1));
    }
    
    return 0;
}
int isInCard(int card,int *cardList,int s,int e){
    int mid = (s+e)/2;

    if (card == cardList[mid])
        return 1;
    if (e<s)
        return 0;
    if(card>cardList[mid])
        return isInCard(card,cardList,mid+1,e);
    if(card<cardList[mid])
        return isInCard(card,cardList,s,mid-1);

}
