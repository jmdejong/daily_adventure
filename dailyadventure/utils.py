import os

def write_safe(filename, data, tempname=None, mode=0o644):
    if tempname is None:
        tempname = filename + ".tempfile"
    with open(tempname, 'w') as f:
        f.write(data)
    os.chmod(tempname, mode)
    os.rename(tempname, filename)
