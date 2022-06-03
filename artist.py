from functools import *

from song import Song
from album import Album

class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getBirthYear(self):
        return self.__birthYear
    def getAlbums(self):
        return self.__albums
    def getSingle(self):
        return self.__singles

    def __overall(self):
        overall = []
        for album in self.__albums:
            overall += [song for song in album.getSongs()]
        overall += self.__singles
        return overall

    def __likedSongAUX(self, bool):
        temp_album = Album(" ", 0)
        [temp_album.addSong(song) for song in self.__overall()]
        return temp_album.sortByPopularity(bool)[0]

    def leastLikedSong(self):
        return self.__likedSongAUX(False)

    def mostLikedSong(self):
        return self.__likedSongAUX(True)

    def totalLikes(self):
        return reduce((lambda x, y : x + y), [song.getLikes() for song in self.__overall()], 0)

    def __str__(self):
        return "Name:" + self.__firstName + " " + self.__lastName + ",Birth year:" + str(self.__birthYear) +\
               ",Total likes:" + str(self.totalLikes())


# rattlestarSong = Song('1___1', 1,1,11)
# majorSong = Song('2___2', 2, 2,0)
# queenSong = Song('3___3', 3, 3, 3)
#
# firstB = Song('4___4', 4)
# secondB = Song('5___5', 5)
# singles = [Song('6___6', 6,6,6), Song('7___7', 7)]
#
# a = Album("1", 1)
# b = Album("2", 2)
#
# a.addSong(rattlestarSong, majorSong, queenSong)
# b.addSong(firstB,secondB)
# albums = [a,b]
#
# artist = Artist("Yo", "Yoyo", 1917, albums, singles)
#
# print(artist.mostLikedSong())
# print(artist.leastLikedSong())
# print(artist.totalLikes())
# print(artist)
