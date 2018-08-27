# include<stdio.h>
# include<stack>
# include<queue>
using namespace std;
stack<int> myStack;
queue<char> myQ;

int main(){
    int n;scanf("%d",&n);
    int num;
    int k = 1;
    for(int i = 0;i<n;i++){
        scanf("%d",&num);
        while(k<=num){
            myStack.push(k);
            myQ.push('+');
            k++;
        } 
        if (myStack.top() != num || myStack.empty()){
            printf("NO\n");
            return 0;
        }
        myStack.pop();
        myQ.push('-');
    }
    while(!myQ.empty()){
        printf("%c\n",myQ.front());
        myQ.pop();
    }
    return 0;
}
