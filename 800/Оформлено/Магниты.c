#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int last;
    scanf("%d", &last);
    int res = 1;
    for (int i = 1; i < n; i++) {
        int cur;
        scanf("%d", &cur);
        if (cur != last)
            res += 1;
        last = cur;
    }
    printf("%d", res);
}
