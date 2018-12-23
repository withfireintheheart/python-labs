def file_search(file_tree, filename):
    try:
        path = file_tree[0] + "/"
        if filename in file_tree:
            return path + filename
        for node in file_tree:
            if isinstance(node, list):
                if len(node) > 1:
                    inner_path = file_search(node, filename)
                    if path is not None:
                        path = path + inner_path
                    return path
        return False
    except TypeError:
        return False


if __name__ == '__main__':
    print(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
    print(file_search(['/tmp', ['1', ['2', ['3', ['4', ['5', 'key1', 'key2', 'key3']]]]]], 'key3'))