// You are using GCC
#include <iostream>
using namespace std;
int main()
{
    int size;
    cin>>size;
    if(size<100 && size>0)
    {
     int array[size]={};
    int sum=0,product=1;
    for(int i =0;i<size;i++)
    {
        cin>>array[i];
        sum+=array[i];
        product*=array[i];
    }
    cout<<"Sum:"<<sum<<"\nProduct:"<<product<<endl;
    }
    else cout<<"Invalid"<<endl;
    return 0;
    
}
