def make_album(artist, title, n_songs=None):
    album = {}
    album['artist'] = artist.title()
    album['title'] = title.title()
    if n_songs:
        album['number of songs'] = n_songs

    return album


while True:
    print("\nEnter the artist's name and album's title to create new album")
    print("Enter 'quit' to exit")

    artist = input('Artist: ')
    if artist == 'quit':
        break

    title = input('Title: ')
    if title == 'quit':
        break

    print(make_album(artist, title=title))
