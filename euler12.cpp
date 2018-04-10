#include <iostream>
#include <vector>

inline int nth_triangle(int n) {
    return n * (n+1) / 2;
}

int count_divisors(int number) {
    std::vector<int> divisor_test(number/2, 1);
    std::size_t divisor_count = 0;
    std::size_t i = 0;
    while(i < divisor_test.size()) {
        if(divisor_test[i] == 1) {
            int divisor = i + 1;
            if(number % divisor == 0)
                divisor_count++;
            else {
                int non_divisor = divisor;
                while(non_divisor < number/2 + 1) {
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
        // triangle = nth_triangle(triangle_index);
        triangle += triangle_index;
        divisor_count = count_divisors(triangle);
        std::cout << triangle << ' ' << divisor_count << std::endl;
        triangle_index++;
    }
    return triangle;
}
int main(void) {
    std::cout << triangle_over_x_divisors(500) << std::endl;
    return 0;
}