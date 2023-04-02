import sys
import json

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def routes(S, direction):
    if obstacle(S, direction) == True:
        if "N" in direction[0]:
            if 0 <= S[0]-int(direction[1]):
                S = [S[0]-int(direction[1]), S[1]]
                return S
        elif "S" in direction[0]:
            cnt = S[0]+int(direction[1])
            if len(p_ls)-1 < cnt:
                return S
            S = [S[0]+int(direction[1]), S[1]]
            return S
        elif "W" in direction[0]:
            if 0 <= S[1]-int(direction[1]):
                S = [S[0], S[1]-int(direction[1])]
                return S
        elif "E" in direction[0]:
            cnt = S[1]+int(direction[1])
            if len(p_ls[0])-1 < cnt:
                return S
            S = [S[0], S[1]+int(direction[1])]
            return S
        return S
    elif obstacle(S, direction) == False:
        return S

def obstacle(S, direction):
        for i in range(int(direction[1])):
            if direction[0] == "S":
                if S[0]+i > len(p_ls):
                    return False
                ob = p_ls[S[0]+i][S[1]]
            elif direction[0] == "N":
                if S[0]-i < 0:
                    return False
                ob = p_ls[S[0]-i][S[1]]
            elif direction[0] == "E":
                if S[1]+i > len(p_ls[0]):
                    return False
                ob = p_ls[S[0]][S[1]+i]
            elif direction[0] == "W":
                if S[1]-i < 0:
                    return False
                ob = p_ls[S[0]][S[1]-i]
            if ob == "X":
                return False
        return True

def DFS(L, res):
    print(res)
    if L == len(r_ls):
        sys.exit(0)
    else:
         S = routes(res, r_ls[L])
         if S == False:
            DFS(L+1, res)
         else:
            DFS(L+1, S)

if __name__ == "__main__":
    p_str = input()
    p_ls = json.loads(p_str)
    r_str = input()
    r_str = r_str.replace(' ', '')
    r_ls = json.loads(r_str)
    res = [0, p_ls[0].index("S")]
    DFS(0, res)
    print(res)