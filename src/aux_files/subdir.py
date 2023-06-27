import os
import fnmatch

def subdir(name='*'):
    """
    Recursively searches for files in the specified directory and its subdirectories.

    Parameters
    ----------
    name : str, optional
        Pathname or filename for search, can be absolute or relative and wildcards (*) are allowed.
        If omitted, the files in the current working directory and its child folders are returned.

    Returns
    -------
    files : list of dicts
        List of files with the following fields:
            name : str
                Full filename
            date : str
                Modification date timestamp
            bytes : int
                Number of bytes allocated to the file
            isdir : bool
                True if name is a directory; False if not.

    Examples
    --------
    >>> a = subdir(os.path.join(os.environ['MATLABROOT'], 'toolbox', 'matlab', '*.mat'))
    >>> a[1]
    {'name': '/Applications/MATLAB73/toolbox/matlab/audiovideo/chirp.mat',
     'date': '14-Mar-2004 07:31:48',
     'bytes': 25276,
     'isdir': False}

    """
    folder, filter = os.path.split(name)
    if not folder:
        folder = os.getcwd()
    if not filter:
        folder, filter = name, '*'

    files = []
    for root, dirs, filenames in os.walk(folder):
        for filename in fnmatch.filter(filenames, filter):
            fullname = os.path.join(root, filename)
            stat = os.stat(fullname)
            files.append({
                'name': fullname,
                'date': str(stat.st_mtime),
                'bytes': stat.st_size,
                'isdir': False if os.path.isfile(fullname) else True
            })

    return files
    
    
    
    #Note that there are some differences between the MATLAB code and the Python implementation. First, the MATLAB code uses the genpath function to generate a list of all subfolders in the specified directory, whereas the Python implementation uses the built-in os.walk function to recursively traverse the directory tree. Second, the MATLAB code uses the cellfun function to apply a function to each element of a cell array, whereas the Python implementation uses a list comprehension. Finally, the MATLAB code uses a struct array to store the list of files, whereas the Python implementation uses a list of dictionaries.