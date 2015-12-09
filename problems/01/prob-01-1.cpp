//advent of code problem 1
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int floor = 0;
    char c;
    while(c = getchar()) {
        if(c == '(') {
            floor++;
        } else if (c == ')') {
            floor--;
        } else {
            break;
        }
    }
    cout << endl << floor << endl;
    return 0;
}
