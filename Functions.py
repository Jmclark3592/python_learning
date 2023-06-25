#Functions

def make_album(artist_name, album_title):
    album = {artist_name : album_title}
    return album

album = make_album('justin clark', 'happy days')

print(album)