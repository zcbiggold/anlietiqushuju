def iterdatainfile(filename, spliter='\t'):
    with open(filename, 'rt') as handle:
        for ln in handle:
            yield ln.split(spliter)


focue, LF = 3, '\n'
with open("output.txt", 'wt') as handle:
    handle.writelines([row[focue] + LF
                       for row in iterdatainfile('text.txt',
                                                 spliter='|')])