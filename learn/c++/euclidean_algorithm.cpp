#include <iostream>

int a,b,divisor,remainder,divided;

int main(){
	std::cin>>a>>b;
	divided=a;
	divisor=b;
	remainder=divided%divisor;
	while (remainder!=0){
		divided=divisor;
		divisor=remainder;
		remainder=divided%divisor;
	}	
	std::cout<<divisor<<'\n'<<a*b/divisor;
}
