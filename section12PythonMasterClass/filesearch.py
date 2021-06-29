import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


# passing one generator as argument
def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # path not the name of the album
            yield song


album_list = find_albums("notmusic", "Aerosmith")
song_list = find_songs(album_list)
for a in song_list:
    print(a)

# retrieve all song where in beginning is word Black, on linux fnmatch is key sensetive
album_list = find_albums("notmusic", "Black*")
song_list = find_songs(album_list)
for a in song_list:
    print(a)
