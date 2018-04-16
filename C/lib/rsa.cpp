#include "rsa.h"

RSA::RSA(){
    srand (static_cast <unsigned> (time(0)));
    generate_keys();
}

int RSA::get_private_key(){
    return this->d;
}


std::vector<int> RSA::get_public_keys(){
    std::vector<int> vec;
    vec.push_back(this->n);
    vec.push_back(this->e);
    return vec;
}


std::vector<int> RSA::chy(std::string string){
    std::vector<int> ret;
    for(char letter : string){
        int ascii = ord(letter);
        int crip = pow(ascii, this->e);
        crip = mod(crip, this->n);
        ret.push_back(crip);
        std::cout << letter<<" "<<crip << std::endl;
    }
    return ret;
}


std::string RSA::unchy(std::string){
    
}


void RSA::generate_keys(){
    this->p = generate_prime();
    this->q = generate_prime();
    this->n = p*q;
    int y = totient(p);
    int x = totient(q);
    this->toti_n = x * y;
    this->e = generate_e();
    this->d = generate_private_key();
}


int RSA::totient(int n){
    if(isprime(n)){
        return n - 1;
    }
}


bool RSA::isprime(int n){
    // Corner cases
    if (n <= 1)  return false;
    if (n <= 3)  return true;

    // This is checked so that we can skip 
    // middle five numbers in below loop
    if (n%2 == 0 || n%3 == 0) return false;

    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
           return false;

    return true;
}


int RSA::generate_e(){
    while(true){
        int generated = this->generate_random(2, toti_n);
        if(this->mdc(this->toti_n, generated) == 1){
            return generated;
        }
    }
}

int RSA::mdc(int x, int y){
    int rest = 1;
    while(y != 0){
        rest = x%y;
        x = y;
        y = rest;
    }
    return x;
}


int RSA::ord(char c){
    return (int) c;
}


char RSA::chr(int i){
    return (char) i;
}


int RSA::generate_prime(){
    int e;
	do{
		e = generate_random();
	}while(!isprime(e));
    return e;
}

int RSA::generate_random(int from, int to){
	return from + (rand()%to);
}

int RSA::mod(int x, int y){
    if(x < y){
        return x;
    }
    return x%y;
}


int RSA::generate_private_key(){
    int d = 0;
    while(mod(d*this->e, this->toti_n) != 1){
        d++;
    }
    return d;
}

