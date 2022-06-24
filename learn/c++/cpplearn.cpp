#include <iostream>

int k,n,lbound,rbound,midpos;

int num(int arr[],int div,int len){
	int res=0;
	for (int j=0;j<len;j++){
		res+=arr[j]/div;
	}
	return res;
}

int main(){
	std::cin>>k>>n;
	int ser[k];
	for (int i=0;i<k;i++){
		std::cin>>ser[i];
	}
	
	lbound=1;
	rbound=1000000;
	while (lbound!=rbound){
		midpos=(lbound+rbound)/2;
		if (num(ser,midpos,k)>n){
			lbound=midpos;			
		}
		else {
			rbound=midpos;
		}
	}
	std::cout<<lbound;
	return 0;
}
