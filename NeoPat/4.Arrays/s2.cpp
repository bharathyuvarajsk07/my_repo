#include<iostream>
using namespace std;
int main()
{
    int n,i,j=0;
    cin>>n;
    int a[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<n;i=i+2)
    {
        if(a[i]<a[i+1])
        {
            j=j+a[i];
        }
        else
        {
            j=j+a[i+1];
        }
    }
    cout<<j;
    return 0;
}
