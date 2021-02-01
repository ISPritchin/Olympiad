#include <stdio.h>

int main() {

    int a[200001];
    int b[200001];

    int n_sets;
    scanf("%d", &n_sets);
    while (n_sets--) {
        int n;
        scanf("%d", &n);

        int value;
        int max_value = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &value);
            if (value > max_value)
                max_value = value;
            a[value] += 1;
            b[i+1] = value;
        }

        int res_v = 0;
        for (int i = 1; i <= max_value; i++) {
            if (a[i] == 1) {
                res_v = i;
                break;
            }
        }

        if (res_v == 0)
            printf("-1");
        else {
            for (int i = 0; i <= n; i++) {
                if (b[i] == res_v) {
                    printf("%d", i);
                    break;
                }
            }
        }

        for (int i = 0; i <= n; i++) {
            a[i] = 0;
            b[i] = 0;
        }

        puts("");
    }
}
