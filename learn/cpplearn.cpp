#include <iostream>

using namespace std;

int main(){
    int num=13;
    bool x=true;
    int res=0;
    for (int i=1;i<=num;i++){
        if (num%i==0){
            res++;
        }
    }
    if (res==2){
        x=true;
    }
    else{
        x=false;
    }
    cout<<x;
    return 0;
} 