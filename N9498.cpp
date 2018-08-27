# include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    if (n <= 59)
        printf("F\n");
    else if(n <= 69)
        printf("d\n");
    else if(n <= 79)
        printf("C\n");
    else if(n <= 89)
        printf("B\n");
    else
        printf("A\n"); 
    return 0;
}
