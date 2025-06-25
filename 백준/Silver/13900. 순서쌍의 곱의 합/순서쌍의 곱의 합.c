#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int user_list[N];
    long long total = 0; 
    long long sum = 0;

    for (int i = 0; i < N; i++) {
        scanf("%d", &user_list[i]);
        sum += user_list[i];
    }

    for (int i = 0; i < N; i++) {
        sum -= user_list[i];
        total += user_list[i] * sum;
    }

    printf("%lld\n", total);
    return 0;
}
