#include <iostream>
using namespace std;

int search(int arr[], int x)
{
    int prev = 0;
    int next = 1;
    while (arr[next] < x)
    {

        if (arr[next] == x)
        {
            return next;
        }
        if (arr[next] < x)
        {

            prev = next;
            next = next + 2;
        }
    }
    if (arr[(prev + next) / 2] == x)
    {
        cout << "index of element is: ";
        return (prev + next) / 2;
    }
    else
    {
        return -1;
        cout << "<element not found";
    }
}

// taking array input and getting output via calling function
int main()
{
    int size;
    cin >> size;
    int *input = new int[size];

    for (int i = 0; i < size; ++i)

    {
        cin >> input[i];
    }
    int element;
    cin >> element;
    cout << search(input, element) << endl;
}