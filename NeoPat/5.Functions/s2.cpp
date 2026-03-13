#include<iostream>
using namespace std;
void calc(int n1, int n2)
{
    int sum =0, pdt=0;
    sum = n1+n2;
    pdt = n1*n2;
    cout << "Sum: " << sum << endl << "Product: " << pdt;
}
int main()
{
    int a,b;
    cin >> a >> b;
    if(a>=256 || a<=-256 ||b>=256 ||b<=-256)
    {
        cout << "Invalid";
        return 0;
    }
    calc(a,b);
    return 0;
}
