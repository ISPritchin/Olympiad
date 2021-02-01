#include <stdio.h>

int main() {

    int n_sets;
    scanf("%d", &n_sets);

    int a[2*100000];
    while (n_sets--) {
        int n;
        scanf("%d", &n);

        for (int i = 0; i < 2*n+1; i++)
            a[i] = 0;

        int x;
        for (int i = 0; i < n; i++) {
            scanf("%d", &x);
            x -= 1;
            if (a[x] == 0)
                a[x]++;
            else if ((x+1 < 2*n+1) && (a[x+1] == 0)) {
                a[x+1]++;
            }
        }

        int res = 0;
        for (int i = 0; i < 2*n+1; i++) {
            if (a[i] != 0) {
                res++;
            }
        }
        printf("%d\n", res);
    }

    return 0;
}