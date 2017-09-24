# -*-coding:utf-8 -*-

def n_3(n):
    if n ==1:
        return 3
    print(n)
    return n + n_3(n-1)

def main():
    a=n_3(6)
    print(a)
    b = [ b for i in range(1,7): b+=i]
    print(b)
            

if __name__ == "__main__":
    main()
