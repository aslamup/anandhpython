# Write a function treemap to map a function over nested list.

def treemap(f,l):
    for i in range(len(l)):
        if isinstance(l[i],list):
            treemap(f,l[i])
        else:
            result.append(x*x)
    return result
print treemap([1, 2, [3, 4, [5]]])
