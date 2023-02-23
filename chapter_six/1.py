import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def f_bin(x):
    if x > 0:
        f_bin(x // 2)
        print(x % 2)

if __name__ == "__main__":
    n = int(input())
    f_bin(n)
