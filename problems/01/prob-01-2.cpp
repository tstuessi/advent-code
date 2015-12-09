//advent of code problem 1
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int floor = 0;
    int counter = 0;
    char c;
    while(c = getchar()) {
        counter++;
        if(c == '(') {
            floor++;
        } else if (c == ')') {
            floor--;
        } else {
            break;
        }
        if(floor == -1) {
            cout << "Got to -1: " << counter << endl;
        }
    }
    cout << endl << floor << endl;
    return 0;
}
