from functools import reduce

from song import Song
class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getSongs(self):
        return self.__songs


    def addSong(self, *songs):
        i = 0
        for song in songs:
            addSongAux = list(filter((lambda x: x.getTitle() == song.getTitle()
                                                      and x.getReleaseYear() == song.getReleaseYear()
                                                      and x.getDuration() == song.getDuration()),self.__songs))
            if(len(addSongAux) == 0):
                self.__songs.append(song)
                i +=1
        return i

    def sortBy(self, byKey, reverse):
        return list(sorted(self.__songs, key = lambda x:  byKey(x), reverse = reverse))

    def sortByName(self, reverse):
        return self.sortBy(Song.getTitle, reverse)

    def sortByPopularity(self, reverse):
        return self.sortBy(Song.getLikes, reverse)

    def sortByDuration(self, reverse):
        return self.sortBy(Song.getDuration, reverse)

    def sortByReleaseYear(self, reverse):
        return self.sortBy(Song.getReleaseYear, reverse)

    def __str__(self):
        return "Title:" + self.getTitle() + ",Release:" + str(self.__releaseYear) + ",songs:{" + ("|".join(map(str, self.__songs))) +  "}"

# rattlestarSong = Song('Snake Jazz', 1989)
# majorSong = Song('Space Oddity', 1969, 315)
# queenSong = Song('Teo Torriatte', 1977, 355, 132178)
#
# a = Album("Green side", 1976)
# a.addSong(rattlestarSong, majorSong, queenSong)
# print(a)
ab = [1,2,3]

print(list(map(lambda x: x + 1, ab)))