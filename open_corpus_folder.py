import os, sys

def open_corpus_folder(path):
    path = path
    dirs = os.listdir(path)
    file_list = []
    for file in dirs:
        if file.endswith('.txt'):
            file_list.append("{}{}".format(path,file))
    all_items = []
    for file in file_list:
        with open(file, 'r') as read_file:
            all_items.append("""{}""".format(read_file.read()))
    all_items_f = []
    for item in all_items:
        all_items_f.append(u' '.join(item.split()).lower())
    for item in all_items_f:
        if item is '':
            all_items_f.remove(item)
            
    return all_items_f
        
