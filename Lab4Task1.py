from collections import OrderedDict

def clean_list(list_to_clean):
    return list(OrderedDict.fromkeys(list_to_clean))

if __name__ == '__main__':
    print(clean_list([32, 32.1, 32.0, -123]))