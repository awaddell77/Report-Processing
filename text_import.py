def text_import(x, mode='utf-8'):
    #reads text file as generator
    words = ''
    l = []
    with open(x, 'r') as f:
        data = f.readlines()
        for line in data:
            if not line: continue
            yield line
def text_process(fname, delim='\t'):
    #returns list of lists separated by the delim
    data = text_import(fname)
    lst = []
    for elem in data:
        if delim != '\n': temp = elem.replace('\n', '')
        items = temp.split(delim)
        temp_lst = []
        for i in range(0, len(items)):
            temp_lst.append(items[i])
        if temp_lst: lst.append(temp_lst)
    return lst


