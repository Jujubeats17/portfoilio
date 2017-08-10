import random
def names():
    fn = ["Sanjana", "Ericka", "Sylvia", "Orli", "Brittany","Yuki", "Hananah", "Leyla", "Fareeha", "Sarah"]
    return fn[random.randint(0,9)]
    ln = ["Vales", "Brown", "Betancourt", "Bleus", "Hill", "Aquino", "Gaudin", "Hronec", "Powell", "Simpson"]
    return ln[random.randint(0,9)]
    random.shuffle(fn, ln)
print(names())
