# include<stdio.h>
# include<vector>
# include<string>
# define MYFLUSH while(getchar() != '\n');
char maxVal[11] = "0123456789";
char minVal[11] = "9876543210";
using namespace std;
vector<int> a;
char arr[11];
void getAns(int *,int,int);
int main(){
    int n;
    char c;
    scanf("%d",&n);
    MYFLUSH
    for(int i = 0;i<n;i++){
        scanf("%c",&c);
        if(c == '<')
            a.push_back(1);
        else
            a.push_back(0);
        scanf("%c",&c);
    }
    maxVal[n+1] = '\0';
    minVal[n+1] = '\0';
    arr[n+1] = '\0';
    int numArr[10] = {0,1,2,3,4,5,6,7,8,9};
    getAns(numArr,n+1,0);
    printf("%s\n%s\n",maxVal,minVal);
}
void getAns(int* numArr,int n,int i){
    if (i==n){
        if (strcmp(maxVal,arr)<0){
            strcpy(maxVal,arr);
        }
        if (strcmp(minVal,arr)>0){
            strcpy(minVal,arr);
        }
        return ;
    }
    for(int idx = 0;idx<10;idx++){
        if(i-1 >= 0 && a[i-1] == 1 && arr[i-1]>= idx+48){
            continue;
           
        }else if (i-1 >= 0 && a[i-1] == 0 && arr[i-1]<=idx+48){
            continue;
        }
        if(numArr[idx] != -1){
            int temp = numArr[idx];
            numArr[idx] = -1;
            arr[i] = (char)(48+idx);
            getAns(numArr,n,i+1);
            numArr[idx] = temp;
        }
    }

}

