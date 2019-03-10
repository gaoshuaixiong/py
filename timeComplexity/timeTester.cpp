#include <iostream>
#define SIZE 10000
 
using namespace std;
 

 
long long get_sum(int n)
{
long long lResult = 0;
for(int i = 0; i < n ; i ++)
{
     for(  int j = 0; j < n; j ++)
     {
            lResult += (long long) ( i * j );
     }
}
return lResult;
}
 
 
int main(void) {
	get_sum(SIZE);
}