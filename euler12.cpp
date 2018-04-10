#include <iostream>
#include <vector>
#include <cmath>

int count_divisors(long long  number) {
    std::vector<long long> divisor_test(std::ceil(std::sqrt(number)), 1);
    std::size_t divisor_count = 0;
    std::size_t i = 0;
    while(i < divisor_test.size()) {
        if(divisor_test[i] == 1) {
            int divisor = i + 1;
            if(number % divisor == 0) {
                divisor_count += 2;
            }
            else {
                long long non_divisor = divisor;
                while(non_divisor < divisor_test.size()) {
                    divisor_test[non_divisor - 1] = 0;
                    non_divisor += divisor;
                }
            }
        }
        i++;
    }
    return divisor_count + 1;
}

int triangle_over_x_divisors(int x) {
    int divisor_count = 0;
    int triangle_index = 1;
    int triangle = 0;
    while(divisor_count <= x) {
        triangle += triangle_index;
        divisor_count = count_divisors(triangle);
        triangle_index++;
    }
    return triangle;
}
int main(void) {
    std::cout << triangle_over_x_divisors(500) << std::endl;
    return 0;
}
