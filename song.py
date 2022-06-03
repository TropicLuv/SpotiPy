
class Song:
    def __init__(self, title, releaseYear, duration=60, likes=0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__likes

    def getDuration(self):
        return self.__duration

    def getLikes(self):
        return self.__likes

    def setDuration(self, num):
        if 720 < num < 0 or num == self.__duration:
            return False
        else:
            self.__duration = num
            return True

    def like(self):
        self.__likes += 1

    def dislike(self):
        self.__likes -= 1

    def __str__(self):
        return "Title:" + str(self.__title) + ",Duration:" + str(self.__duration/60) + " minutes,Release year:" +\
               str(self.__releaseYear) + ",Likes:" + str(self.__likes)

