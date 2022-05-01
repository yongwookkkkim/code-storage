#include <iostream>

unsigned int n, k, midpos;
unsigned int lbound=1, rbound=2147483647, res=0;

int main(){
	std::cin>>k>>n;
	unsigned int wires[k];
	for (int i=0; i<k; i++){
		std::cin>>wires[i];
	}
	while (lbound<rbound){
		res=0;
		midpos=(lbound+rbound)/2;
		for (int j=0; j<sizeof(wires)/sizeof(wires[0]); j++){
			res+=wires[j]/midpos;
		}
		if (res>=n){
			lbound=midpos;
		}
		else{
			rbound=midpos;
		}
	}
	std::cout<<rbound;
	return 0;
}
