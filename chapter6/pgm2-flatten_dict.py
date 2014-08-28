# Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(d,result=None,y=[]):
    if result is None:
        result={}
    for k,v in d.items():
        if isinstance(v,dict):
            flatten_dict(v,result,y+[k])
        else:
            result['.'.join(y+[k])] = v
    return result    
print flatten_dict({'a': 1, 'b': {'x':2,'y': 3}, 'c': 4})
