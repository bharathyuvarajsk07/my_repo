#include<iostream>
using namespace std;
int increment(int a);
int main(){
    int x;
    cin >> x;
    int a=increment(x);
    cout << a;
    return 0;
}
int increment(int x){
    x=x+1;
    return x;
}
