#include <iostream>
using namespace std;
int add(int, int);

int main() {
	int a=10, b=20;
	cout << "Hello World" << endl;
	cout << "a + b = " << add(a, b) << endl;
	return 0;
}


int add(int a, int b) {
	return a+b;
}
