
def create_list(x, count):
    y = []
    for z in range(count):
        y.insert(z,x)
    return y

def create_dict(kv):
    d = {}
    for key, val in kv:
        d[key] = val
    return d

def append_element_to_list(x, y=()):
    y = list(y)
    y.append(x)
    return y