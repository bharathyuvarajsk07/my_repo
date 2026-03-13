// You are using GCC
#include <iostream>
using namespace std;
main()
{
    int size;
    int array[size];
    for(int i=0;i<size;i++)
    {
        cin>>array[i];
    }
    int numcount=0;
    int index=-1;
    for(int i =0;i<size;i++)
    {
        int count;
        for(int j=0;j<size;j++)
        {
            if(array[i]==array[j])
            {
                count++;
            }
        }
        if(count> numcount)
        {
            numcount=count;
            index=i;
        }
    }
    if(numcount>size/2) cout<<array[index]<<endl;
    else cout<<'0'<<endl;
    return 0;
    
}
