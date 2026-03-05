// You are using GCC
#include <iostream>
using namespace std;
int main()
{
    int size;
    cin>>size;
    if(size>0 && size<=10)
    {
    long int array[size]={},max=0,min=99,temp;
    for(int i=0;i<size;i++)
    {
        cin>>array[i];
        temp=array[i];
        if(min>temp)
        {
            min=temp;
        }
        if(max<temp)
        {
            max=temp;
        }
    }
    cout<<"Max:"<<max<<"\nMin:"<<min<<endl;
    }
    else cout<<"Invalid"<<endl;
}
