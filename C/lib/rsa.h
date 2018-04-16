#ifndef RSA_H
#define RSA_H

#include<vector>
#include<string>
#include <math.h>
#include <iostream>


class RSA{
public:
    RSA();
    int get_private_key();
    std::vector<int> get_public_keys();
    std::vector<int> chy(std::string string);
    std::string unchy(std::string string);

private:
    void generate_keys();
    int generate_private_key();
    bool isprime(int n);
    int totient(int n);
    int generate_prime();
    int generate_random(int from=2, int to=pow(2, 10));
    int generate_e();
    int mdc(int x, int y);
    int mod(int x, int y);
    int ord(char c);
    char chr(int i);

    int p, q, n, toti_n, e, d;
};


#endif