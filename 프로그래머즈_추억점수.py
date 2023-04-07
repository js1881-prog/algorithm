name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    ls = []
    res = 0
    for p in photo:
        for s in p:
            if s in name:
                res += yearning[name.index(s)]
        ls.append(res)
        res = 0
    return ls
    

solution(name, yearning, photo)
