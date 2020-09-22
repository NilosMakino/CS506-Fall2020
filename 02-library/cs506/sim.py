import math

def euclidean_dist(x, y):
    if (x == [] or y == []):
        return ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        return ValueError("lengths must be equal") 
    
    sum = 0
    for i in range(len(x)):
        sum += ((x[i] - y[i]) ** 2)
    return (sum ** .5)

def manhattan_dist(x, y):
    if (x == [] or y == []):
        return ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        return ValueError("lengths must be equal") 
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i] - y[i])
    return sum

def jaccard_dist(x, y):
    if (x == [] or y == []):
        return ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        return ValueError("lengths must be equal") 
    return 1 - (len(set(x) & set(y))/len(set(x) | set(y)))

def cosine_sim(x, y):
    if (x == [] or y == []):
        return ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        return ValueError("lengths must be equal") 
    dot_prod = 0
    xsum = 0
    ysum = 0
    for i in range(len(x)):
        dot_prod += (x[i]*y[i])
        xsum += x[i]**2
        ysum += y[i]**2
    return dot_prod/((xsum*ysum)**.5)
    

# Feel free to add more
