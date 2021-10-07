#include<bits/stdc++.h>
using namespace std;

int main()
{
    int size;
    cout<<"Enter the size of the array: ";
    cin>>size;
    int arr[size];
    for(int i=0;i<size;i++)
    {
        cout<<"Enter the element: ";
        cin>>arr[i];
    }
    int x;
    cout<<"Enter the element to find: ";
    cin>>x;
    int low=0,high=size-1,mid;
    while(low<=high)
    {
        mid = low + (high-1)/2;
        if(arr[mid]==x)
        {
            cout<<"Element found at index: "<<mid;
            break;
        }
        else if(arr[mid]>x)
        {
            high=mid-1;
        }
        else
        {
            low=mid+1;
        }
    }
    if(low>high)
    {
        cout<<"Element not found";
    }
    return 0;
}
