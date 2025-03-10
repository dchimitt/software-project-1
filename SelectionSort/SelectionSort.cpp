#include <iostream>
using namespace std;

int main() {
    int elementQuantity;
    cout << "Enter the number of elements: ";
    cin >> elementQuantity;
    int Elements[elementQuantity];
    cout << "Enter the elements: ";
    for (int i = 0; i < elementQuantity; i++) {
        cin >> Elements[i];
    }

    // Selection sort algorithm
    for (int i = 0; i < elementQuantity-1; i++) {
        int minimumValuePosition = i;
        for (int j = i+1; j < elementQuantity; j++) {
            if (Elements[j] < Elements[minimumValuePosition]) {
                minimumValuePosition = j;
            }
        }
        // Swap the found minimum element with the first element
        int temp = Elements[minimumValuePosition];
        Elements[minimumValuePosition] = Elements[i];
        Elements[i] = temp;
    }

    cout << "Sorted array: ";
    for (int i = 0; i < elementQuantity; i++) {
        cout << Elements[i] << " ";
    }
    cout << endl;
    return 0;
}