import os

def write_safe(filename, data, tempname=None):
    if tempname is None:
        tempname = filename + ".tempfile"
    with open(tempname, 'w') as f:
        f.write(data)
    os.rename(tempname, filename)
