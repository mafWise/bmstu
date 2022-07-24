#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int secs;

    printf("Enter the time in seconds: ");

    if (scanf("%d", &secs) != 1)
       return EXIT_FAILURE;

    int ours = secs / 3600;
    secs = secs - ours * 3600;
    int mins = secs / 60;
    secs = secs - mins * 60;

    printf("Result: %d %d %d\n", ours, mins, secs);
    return EXIT_SUCCESS;
}
