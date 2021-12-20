#include <stdio.h>

int main()
{
    int A, B;
    scanf("%d %d", &A, &B);

    if ((0 < A) && (B < 10))
        printf("%d", A - B);
}
