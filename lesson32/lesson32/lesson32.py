#import os
#tree = os.walk('folder')
#print(tree)
#for i in tree:
#   print(files)



def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep) 
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        #print(root, files, level, indent, sub_indent)
        for i in files:
            print(f'{sub_indent}{file}')
read_dir('folder')




