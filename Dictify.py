from C_sort import *
class Dictify:
    def __init__(self, fname):
        self.fname = fname
        self.strip_headers = True

    def main(self):
        #should produce list of dictionaries from a csv, with the column headers as the keys
        item = C_sort(self.fname)
        items = item.contents
        crit = item.contents[0]
        if self.strip_headers: crit = [i.strip(" ") for i in crit]
        results = []
        for i in range(1, len(items)):
            d = dict.fromkeys(crit, 0)
            for i_2 in range(0, len(items[i])):
                d[crit[i_2]] = items[i][i_2]
            results.append(d)
        return results