#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    double xq, yq;
    double xr, yr;
    double xp, yp;
    double eps = 1e-6;
    int ans = 0;

    printf("Enter the xq, yq, xr, yr, xp, yp: ");

    if (scanf("%lf%lf", &xq, &yq) != 2)
        return EXIT_FAILURE;
    if (scanf("%lf%lf", &xr, &yr) != 2)
        return EXIT_FAILURE;
    if (scanf("%lf%lf", &xp, &yp) != 2)
        return EXIT_FAILURE;

    double segments_length = sqrt((xq - xr) * (xq - xr) + (yq - yr) * (yq - yr));
    double l1_from_the_point = sqrt((xq - xp) * (xq - xp) + (yq - yp) * (yq - yp));
    double l2_from_the_point = sqrt((xr - xp) * (xr - xp) + (yr - yp) * (yr - yp));
    double sum_l1_l2 = l1_from_the_point + l2_from_the_point;

    if (segments_length <= eps)
        return EXIT_FAILURE;
    else if (fabs(sum_l1_l2 - segments_length) <= eps)
        ans = 1;
    else
        ans = 0;

    printf("Result: %d\n", ans);
    return EXIT_SUCCESS;
}
