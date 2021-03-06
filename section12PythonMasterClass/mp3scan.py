import os
import fnmatch


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f"*.{extension}"):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)  # use it to yield values


for f in find_music('notmusic', 'emp3'):
    print(f)
