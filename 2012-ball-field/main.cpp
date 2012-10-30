#include <iostream>

#include "field.h"
#include "ball.h"

using namespace std;

int main()
{
    const int WIDTH = 16;
    const int HEIGHT = 12;
    Field* field = new Field(WIDTH, HEIGHT);
    field->add(new Ball(4, 8, +1, +1, WIDTH, HEIGHT));
    field->add(new Ball(12, 4, +1, +1, WIDTH, HEIGHT));
    field->add(new Ball(8, 6, +1, +1, WIDTH, HEIGHT));
    field->print(cout);

    string line;
    while(getline(cin, line)) {
        field->moveAll();
        field->print(cout);
    }

    delete field;
    return 0;
}

