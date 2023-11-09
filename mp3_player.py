import pathlib
import pygame
import eyed3
pygame.init()
pygame.mixer.init()
print("")
print("")

# Dictionaries der Alben
path = pathlib.Path(r"C:\Users\dkomm\Desktop\Weiterbildung\Projekte\mp3_player--practice\mp3 Player")
collection_path = tuple(item for item in path.iterdir())
collection_names = tuple(item.name for item in path.iterdir())
collection_number = tuple(range(len(collection_names)))
dictionary_collection_names = dict(zip(collection_number, collection_names))
dictionary_collection_path = dict(zip(collection_number, collection_path))
# Liste der Alben


def overview_collection():
    for key, val in dictionary_collection_names.items():
        print(f"{key+1} {val}")


def overview_album(p):
    path_a = p
    album_names = tuple(item.name for item in path_a.iterdir())
    album_numbers = tuple(range(len(album_names)))
    dictionary_album_names = dict(zip(album_numbers, album_names))
    for key, val in dictionary_album_names.items():
        print(f"{key+1} {val}")


def navigation_album():
    while True:
        try:
            playmode = str(input("\nAbspielen:\n Ein Lied: Nummer eingeben.\n Gesamtes Album: G eingeben.")).lower()
            if playmode.isdigit():
                playmode = int(playmode)
                return playmode

            elif playmode.isalpha():
                return playmode

        except ValueError:
            print("Fehlerhafte Eingabe")


def playmode_function(p):
    select = p
    if select == "g":
        return 0
    else:
        return select-1


def path_collection():
    while True:
        print("Willkommen in Ihrem mp3 Player")
        print("Welches Album möchten Sie hören?")
        print("")
        overview_collection()
        select = int(input("\n Album Nummer: "))-1
        print("\nIhr gewähltes Album:", dictionary_collection_names[select])
        return dictionary_collection_path[select]


def menu_return():
    menu = str(input("Zurück zum Menü? (j/n)"))
    if menu == "j":
        holistic_function()


def player(p, q):
    relativ_track = 0
    while True:
        album_path = p
        song_path = tuple(item for item in album_path.iterdir())
        song_numbers = tuple(range(len(song_path)))
        dictionary_song_path = dict(zip(song_numbers, song_path))
        print(dictionary_song_path)
        now_playing = dictionary_song_path[q+relativ_track]
        print(now_playing)
        info = eyed3.load(now_playing)
        print("Künstler:\t", info.tag.artist)
        print("Album:\t\t", info.tag.album)
        print("Titel:\t\t", info.tag.title)
        pygame.mixer.music.load(now_playing)
        pygame.mixer.music.play()
        control = str(input("\nN = Nächster Song\nZ = Zurück\nS = Stop  "))

        if control.lower() == "s":
            pygame.mixer.music.stop()
            menu_return()
            break

        if control.lower() == "n":
            relativ_track += 1

        if control.lower() == "z":
            relativ_track -= 1


def holistic_function():
    album_select = path_collection()
    overview_album(album_select)
    player(album_select, playmode_function(navigation_album()))


holistic_function()
