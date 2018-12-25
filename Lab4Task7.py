
def find_most_frequent(text, sep='.,:;!?- '):
    a = {}
    s = ''
    for i in text.lower() + '.':
        if i not in sep:
            s += i
        elif s:
            a[s] = a.setdefault(s,0) + 1
            s = ''
    if not a:
        return False
    m = max(a.values())
    return sorted([i for i in a if a[i] == m])


if __name__ == '__main__':
    print(find_most_frequent('Hello,Hello, my dear!'))
    print(find_most_frequent('to understand recursion you need first to understand recursion...'))