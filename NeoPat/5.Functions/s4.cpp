// You are using GCC
#include <iostream>
using namespace std;
int reverse(int n)
{
    int temp=0,rev,rem;
    while(n>0)
    {
        rem=n%10;
        n=n/10;
        temp=((temp*10)+rem);
    }
    return temp;
}
main()
{
    int a;
    cin>>a;
    cout<<reverse(a);
}
