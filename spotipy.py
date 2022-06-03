from functools import reduce

from album import Album
from artist import Artist
from song import Song

class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *artists):
        self.__artists += list(filter((lambda artist: not any([(artist.getFirstName() == lst_artist.getFirstName()
                                             and artist.getLastName() == lst_artist.getLastName()
                                             and artist.getBirthYear() == lst_artist.getBirthYear())
                                                    for lst_artist in self.__artists ]) ),artists))
    def getTopTrendingArtist(self):
        artist = (list(sorted(self.__artists, key= lambda x: x.totalLikes(), reverse=True))[0])
        return artist.getFirstName(), artist.getLastName()

    def getTopTrendingAlbum(self):
        lst = []
        [[lst.append(album) for album in artist.getAlbums()] for artist in self.__artists]
        return list(sorted(lst, key= lambda x: reduce(lambda i,j : i + j,[song.getLikes() for song in x.getSongs()] ,0), reverse=True))[0].getTitle()

    def getTopTrendingSong(self):
        return list(sorted(self.__artists,key=lambda x: x.mostLikedSong().getLikes(), reverse=True))[0].mostLikedSong().getTitle()

    @staticmethod
    def cleanTextArray (arr):
        arr = list(map(lambda x: x.strip(), arr))
        return arr

    @staticmethod
    def replaceTextArray(arr, chars):
        arr = list(map(lambda x: x.replace(chars, ""), arr))
        return arr

    @staticmethod
    def loadFromFile(direction):
        txt = open(direction, "r").read()
        artists_tem = txt.strip().replace("\n", "").replace("artists:", "")[1::].strip().split("#")
        ret_artists = SpotiPy()

        for artist in artists_tem:
            artist = artist[:-1]
            artist = artist.split("albums:")
            artist = SpotiPy.cleanTextArray(artist)
            artist[0] = artist[0][:-1].split(",")
            artist[1] = (artist[1])[1:]
            artist[1::] = SpotiPy.cleanTextArray(artist[1::])
            artist[1] = artist[1].split("singles:")
            artist[1] = SpotiPy.cleanTextArray(artist[1])
            artist[1][0] = artist[1][0].split("%")
            album_set = []
            singles_t = []
            artist_t = Artist(artist[0][0], artist[0][1], artist[0][2], album_set, singles_t)

            for album in artist[1][0]:
                album = album[0:-2]
                album = album.split(",songs:")
                album = SpotiPy.cleanTextArray(album)
                album = SpotiPy.cleanTextArray(album)
                album = SpotiPy.cleanTextArray(album)
                album[1] = album[1][1:-1]
                album = SpotiPy.cleanTextArray(album)
                album[1] = album[1].split("|")
                album[1] = SpotiPy.cleanTextArray(album[1])
                album[1] = SpotiPy.replaceTextArray(album[1], " minutes")
                album[0] = album[0].split(",")
                album_t = Album(album[0][0],album[0][1])
                album_set.append(album_t)

                for song in album[1]:
                    song = song.split(",")
                    song = SpotiPy.cleanTextArray(song)
                    song_t = Song(song[0],int(song[2]),int(float(song[1])*60),int(song[3]))
                    album_t.addSong(song_t)

            artist[1][1] = artist[1][1][1:-1]
            for single in artist[1][1].split("|"):
                single = single.strip()
                single = single.split(",")
                single = SpotiPy.replaceTextArray(single, " minutes")
                single_t = Song(single[0], int(single[2]), int(float(single[1]) * 60), int(single[3]))
                singles_t.append(single_t)
            ret_artists.addArtists(artist_t)
        return ret_artists






# rattlestarSong = Song('1___1', 1,1,11)
# majorSong = Song('2___2', 2, 2,14)
# queenSong = Song('3___3', 3, 3, 3)
#
# firstB = Song('4___4', 4,4,17)
# secondB = Song('5___5', 5)
# singles = [Song('6___6', 6,6,6), Song('7___7', 7)]
#
# a = Album("1", 1)
# b = Album("2", 2)
# c = Album("3",3)
# d = Album("4",4)
#
# a.addSong(rattlestarSong, majorSong)
# b.addSong(firstB,secondB)
# c.addSong(majorSong, firstB)
# albums = [a,b]
#
#
# artist = Artist("Yo", "Yoyo", 1917, albums, singles)
# artist.totalLikes()
#
# artist1 = Artist("qq", "666", 1917, [c], [])
# artist2 = Artist("Yo", "Yoyoyoyoyo", 1917, [a], [])
# artist3 = Artist("You", "Yoyo", 0000, [d], [firstB, secondB, queenSong])
#
#
# tester = SpotiPy()
# tester.addArtists(artist2)
# tester.addArtists(artist,artist1,artist3)
#
#
# print(tester.getTopTrendingSong())
# a = SpotiPy.loadFromFile("data\data3.txt")
# for artist in a.getArtists():
#     print(artist)
#     for album in artist.getAlbums():
#         print(album)
#     for single in artist.getSingle():
#         print(single)