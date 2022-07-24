#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int var;

    printf("Enter the integer: ");

    if (scanf("%d", &var) != 1)
        return EXIT_FAILURE;
    if (var < 1)
        return EXIT_FAILURE;

    printf("Result: ");
    while (var > 1)
    {
        if (var % 2 == 0)
        {
            var /= 2;
            printf("2");
            if (var > 1)
                printf(" ");
            continue;
        }

        for (int i = 3;i <= var;i += 2)
        {
            if (var % i == 0)
            {
                var = var / i;
                printf("%d", i);
                if (var > 1)
                    printf(" ");
                break;
            }
        }
    }

    printf("\n");
    return EXIT_SUCCESS;
}
