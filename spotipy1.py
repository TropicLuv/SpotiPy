from album import Album
from artist import Artist
from song import Song


class SpotiPy:
    def __init__(self):  # simple constructor which initializes artists with empty list
        self.__artists = []

    def getArtists(self):  # simple getter
        return self.__artists

    def addArtists(self, *singers):  # function which adds artists to artistsList in spotypy class object
        for x in singers:
            toAdd = True
            for y in self.getArtists():
                if (x.sameArtist(y)):
                    toAdd = False
            if toAdd:
                self.__artists.append(x)

    def getTopTrendingArtist(self):  # returns artist with most total likes
        artists = self.getArtists()
        if len(artists) == 0:  # checks whether we have artist if not exception
            raise Exception("You do not have artist,Hence no popular artist exists ")
        toReturn = artists[0]  # if no exception we start counter from first artist and check everyone
        tempInt = artists[0].totalLikes()
        for x in artists:
            if x.totalLikes() > tempInt:
                tempInt = x.totalLikes()
                toReturn = x
        # after loop iteration toReturn contains artist with most likes so i return it in format i want
        return (toReturn.getFirstName(), toReturn.getSecondName())

    def getTopTrendingAlbum(self):
        if len(self.getArtists()) == 0:  # checks whether we have artist if not exception
            raise Exception("You do not have artist,Hence no popular album exists")
        albumToReturn = None  # here we dont even know if one album exists so i make it None
        tempMostLikedAlbum = None  # here we assume
        # loop to find most liked album
        for x in self.getArtists():

            for y in x.getAlbums():
                if (albumToReturn is None):
                    albumToReturn = y
                    tempMostLikedAlbum = y.getToTalLikes()
                else:
                    if y.getToTalLikes() > tempMostLikedAlbum:
                        albumToReturn = y
                        tempMostLikedAlbum = albumToReturn.getToTalLikes()
        if (albumToReturn is None):
            raise Exception("no album in spotypy ")
        return albumToReturn.getTitle()

    def getTopTrendingSong(self):
        artists = self.getArtists()
        if len(artists) == 0:  # checks whether we have artist if not exception
            raise Exception("You do not have artist,Hence no popular song exists")
        songToReturn = None
        tempMaxLikesOnOneSong = None
        for x in artists:
            if songToReturn is None:
                songToReturn = x.mostLikedSong()
                tempMaxLikesOnOneSong = songToReturn.getLikes()
            elif tempMaxLikesOnOneSong < x.mostLikedSong().getLikes():
                songToReturn = x.mostLikedSong()
                tempMaxLikesOnOneSong = songToReturn.getLikes()
        return songToReturn.getTitle()

    def fromStringToSong(songString):
        songString = songString.strip()
        while songString[-1] == '}':
            songString = songString[:-1]
            songString = songString.strip()

        songAtributesList = songString.split(',')
        splitedDuration = songAtributesList[1].split(" ")
        duration = int(float(splitedDuration[0]) * 60)
        return Song(songAtributesList[0], int(songAtributesList[2]), duration, int(songAtributesList[3]))

    def fromStringToAlbum(albumString):
        albumString = albumString[6:]
        albumString = albumString.strip()
        while albumString[0] == '{':
            albumString = albumString[1:]
            albumString = albumString.strip()

        albumSeparated = albumString.split('%')
        albums = []

        for x in albumSeparated:
            separateAtributesAndSongs = x.split('{')
            atributesSplited = separateAtributesAndSongs[0].split(',')
            toAddInList = Album(atributesSplited[0], int(atributesSplited[1]))
            songsStringList = separateAtributesAndSongs[1].split('|')
            for tempSong in songsStringList:
                sng = SpotiPy.fromStringToSong(tempSong)
                toAddInList.addSongs(sng)
            albums.append(toAddInList)
        return albums
    def fromStringToArtist(artistString):
        artistString = artistString.strip()
        listOfUsefulValues = artistString.split(',')
        name = listOfUsefulValues[0]
        lastName = listOfUsefulValues[1]
        birthYear = listOfUsefulValues[2]
        albumsString = listOfUsefulValues[3]
        singlesString = listOfUsefulValues[4]
        singles = []
        singlesString = singlesString[9:]
        singlesList = singlesString.split('|')
        for sng in singlesList:
            singles.append(SpotiPy.fromStringToSong(sng))

        albums = SpotiPy.fromStringToAlbum(albumsString)
        return Artist(name, lastName, birthYear, albums, singles)

    def loadFromFile(path):
        toReturn = SpotiPy()
        file = open(path, "r")
        dataInString = file.read()
        dataInString = dataInString.replace("\n", "")  # remove unnecesary stuff
        dataInString = dataInString[9:]
        artistsList = dataInString.split('#')
        for x in artistsList:
            print()
            print(x)
            # toReturn.addArtists(SpotiPy.fromStringToArtist(x))

        file.close()
        return toReturn


# x = SpotiPy.loadFromFile("data/data0.txt")
a = SpotiPy.fromStringToArtist(
    "    Jarrett,Church,1981,    albums:    {        Shortsighted Client,2018,songs:        {             Each Panics,1.2 minutes,2005,175            |Petri Stiller,0.5 minutes,2012,135        }    },    singles:    {        Winer Retarder Florin,3.1 minutes,2018,109    }")
# alb = SpotiPy.fromStringToAlbum("      {   Biographies,1994,songs:        {             Would Gables,0.9 minutes,1999,78            |Chili Rho,9.9 minutes,2022,161            |Cuisine Video Grimace,7.1 minutes,2020,97            |Axiom Prompter,2.5 minutes,1998,173            |Chemist Comic,4.6 minutes,1993,198        }        %Tonnage,2021,songs:        {             Dunk Protestant Without Surgical,0.3 minutes,2016,7            |Stairways Stamps,3.5 minutes,2003,16            |Repertory Council,5.2 minutes,1998,45            |Swing Trump,9.2 minutes,2006,129        }    }")
# for x in alb:
#     print()
#     print(x)
# x=SpotiPy.fromStringToSong('Each Panics,1.2 minutes,2005,175')
# print(x)
# j= Album("jeeeee",1961)
# print(j.addSongs(Song('A', 2010, 100, 1575), Song('B', 2011, 200, 1570), Song('a', 2012, 300, 7500)))

# er= Album("jeo",1961)
# print(er.addSongs(Song('e', 2010, 100, 3232003999923), Song('r', 2011, 200, 3232003999923), Song('a', 2012, 300, 32)))

# davidBowie= Artist("david","Bowie",1955,[er,j],[Song('B', 2011, 200, 9999),Song('B', 2011, 200, 100001)])
# print(davidBowie.leastLikedSong())
# print(davidBowie)
# print("sdasdadasda")
# test = SpotiPy()
# err= Album("err",1961)
# err.addSongs(Song('eee', 23, 100, 32323999923), Song('r', 2011, 200, 1570), Song('a', 2012, 300, 32))
# niazdiasamidze= Artist("niaz","diasamidze",1955,[err],[Song('eeie', 23, 100, 3232003999923)])
# test.addArtists(davidBowie,niazdiasamidze)
# print(test.getTopTrendingSong())
# print(test.getTopTrendingArtist())
# print("sassadasdas")
# print(test.getTopTrendingAlbum())

