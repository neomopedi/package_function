
def bubble_sort(items):
    for item in range(len(items)-1,0,-1):
        for i in range(item):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items
    '''Return array of items, sorted in ascending order'''

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        return quick_sort([e for e in items[1:] if e <= items[0]]) + [items[0]] +\
            quick_sort([e for e in items[1:] if e > items[0]])
    '''Return array of items, sorted in ascending order'''

    def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        return quick_sort([e for e in items[1:] if e <= items[0]]) + [items[0]] +\
            quick_sort([e for e in items[1:] if e > items[0]])
