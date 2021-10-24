#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

bool losuj()
{
    // trefle - 13
    // jesli wylosujemy trefla funkcja zwraca prawde
    // jesli nie lodujemy dalej z mniejszej ilosci kart gdzie jest tyle samo trefli
    int x = rand() % 52;
    if (x < 13)
    {
        return true;
    }
    int y = rand() % 51;
    if (y < 13)
    {
        return true;
    }
    int z = rand() % 50;
    if (z < 13)
    {
        return true;
    }

    return false;
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));
    // rand 0 - 1
    // double r = ((double) rand() / (RAND_MAX));


    //oczekiwana wartosc 0,5864705882352941
    //ok. 20 mln
        int n = 20000000;
        int d = 10;


        for (int j = 0; j < d; j++)
        {
            int sum = 0;
        for (int i = 0; i < n; i++)
        {
            if (losuj())
            {
                sum++;
            }
        }
        cout << ((double)sum / (double)n) << endl;
        }
        
    return 0;
}
