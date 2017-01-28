fname = str(raw_input('Enter the filename: '))
if fname.split('.')[1] != 'txt':
    print 'Enter a .txt file'
with open(fname,'r') as fp:
    essay = fp.readline()
    print essay