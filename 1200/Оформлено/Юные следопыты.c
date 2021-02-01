#include <stdlib.h>
#include <string.h>
#include <stdio.h>

unsigned exps[200000];

int main() {
    int n_sets, N = 0, x;

    scanf("%d", &n_sets);
    for (int i = 0; i < n_sets; i++) {
        memset(exps, 0, sizeof(unsigned[N]));

        int z = 0, r = 0, n_people;

        scanf("%d", &N);
        for (int j = 0; j < N; ++j) {
            scanf("%d", &x);
            ++exps[x-1];
        }
        for (int j = 0; j < N; ++j) {
            n_people = exps[j];
            z += n_people;
            r += z / (j+1);
            z %= j+1;
        }
        printf("%d\n", r);
    }
}