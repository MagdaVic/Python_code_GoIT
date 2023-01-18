# def to_indexed(source_file, output_file):
#     with open(source_file,'r') as fs:
#         lst_source=fs.readlines()
#     with open(output_file,'w') as fo:
#         fo.writelines(f'{ind}: {el}' for ind,el in enumerate(lst_source))
        
def to_indexed(source_file, output_file):
    with open(source_file,'r') as fs:
        lines=fs.readlines()
    new_l = []
    for i in range(0, len(lines)):
        new_l.append(str(i) + ': ' + lines[i])
    with open(output_file, 'w') as f1:
        for i in new_l:
            f1.write(i)


source_file=r'D:\GitHub\Tutorial\7_module\source_file.py'
output_file=r'D:\GitHub\Tutorial\7_module\output_file.py'
to_indexed(source_file, output_file)