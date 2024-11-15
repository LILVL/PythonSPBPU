# TODO решите задачу

def task() -> float:
    a = 0
    sch = 0
    sum_ = 0
    ch1 = 0
    ch2 = 0
    f = open("input.json", "r")
    a = f.readlines()
    for i in range(len(a)):
        if a[i].find("score") != -1:
            ch1 = float(a[i][((a[i].find("score"))+8):len(a[i])-2])
        elif (a[i].find("weight")) != -1:
            ch2 = float(a[i][((a[i].find("weight"))+9):len(a[i])-1])
        if(ch1 != 0) and (ch2 != 0):
            sum_ += ch1*ch2
            ch1, ch2 = 0, 0
    f.close()
    return round(sum_, 3)

print(task())

