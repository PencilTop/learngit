#include <iostream>
#include <string>
using namespace std;
int add(int, int);
string multistring(string, int);

int main() {
	int a=10, b=20;
	cout << "Hello World" << endl;
	cout << "a + b = " << add(a, b) << endl;
	multistring("hello", 3);
	return 0;
}


int add(int a, int b) {
	return a+b;
}

string multistring(string s, int i) {
	while(i > 0) {
		cout << s << " ";
		i--;
	}
	cout << endl;
}
