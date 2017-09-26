#include <stdio.h>

int main(int argc, char const *argv[])
{
    int dis = 100;
    float power = 2.345f;
    double super_power = 56789.4532;
    char init = 'A';
    char first_name[] = "Zed";
    char last_name[] = "Shaw";

    printf("You are %d miles away\n", dis);
    printf("You have %f levels of power\n", power);
    printf("You have %f awasome super_power\n", super_power);
    printf("I have an init %c\n", init);
    printf("My first_name %s\n", first_name);
    printf("My last_name %s\n", last_name);
    printf("My name is %s %c. %s\n", first_name, init, last_name);
    printf("");
    
    return 0;
}