def make_album(artist, title, n_songs=None):
    album = {}
    album['artist'] = artist.title()
    album['title'] = title.title()
    if n_songs:
        album['number of songs'] = n_songs

    return album


print(make_album('nguyen', 'tuoi 22'))
print(make_album('tran dinh nguyen', 'happy day'))
print(make_album('nguyen tran', 'full house', 10))
