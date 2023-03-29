import sys
import json

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def routes(S, direction):
    if "N" in direction[0]:
        if 0 >= S[1]-direction[1]:
            S = [S[0], S[1]-direction[1]]
            return S
    elif "S" in direction[0]:
        if len(p_ls) >= S[1]+direction[1]:
            S = [S[0], S[1]+direction[1]]
            return S
    elif "W" in direction[0]:
        if 0 >= S[0]-direction[1]:
            S = [S[0]-direction[1], S[1]]
            return S
    elif "E" in direction[0]:
        if len(p_ls[0]) >= S[0]+direction[1]:
            S = [S[0]+direction[1], S[1]]
            return S
    else:
        return False

# def DFS(L, res):
#     if L == len(p_ls+1):
#         print(res)
#         sys.exit(0)
#     else:

if __name__ == "__main__":
    p_str = input()
    p_ls = json.loads(p_str)
    r_str = input()
    r_str = r_str.replace(' ', '')
    r_ls = json.loads(r_str)
    res = [p_ls[0].index("S"), 0]
    DFS(0, res)

