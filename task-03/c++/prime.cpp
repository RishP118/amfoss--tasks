#include<iostream>
using namespace std;
int main()
{
    int n,i,s,c;
    cout<<"Enter n: ";
    cin>>n;
    for(i=2;i<=n;i++)
    {
        c=0;
        for(s=2;s<=i/2;s++)
        {
            if(i%s==0)
            {
                c=1;
                break;

            }

        }
        if(c==0)
        cout<<i<<",";

    }
    return 0;

}
