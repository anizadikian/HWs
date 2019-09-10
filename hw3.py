class Classroom:

    def __init__(self, numberofseats, classromnumber):
        self.nofseats = numberofseats
        self.nclassrom = classromnumber
        self.schedule = []

    def isFree(self, start, end):
        is_Free = True
        for i in self.schedule:
            if end < i["start"] or start > i["end"]:
                pass
            else:
                is_Free = False
                break
        return is_Free

    def reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False


def main():

    myclass = Classroom(30, 212)

    while True:
        start = input("Please insert the start time of your reservation  ")
        end = input("Please insert the end time of your reservation   ")

        if myclass.isFree(start, end) == False:
            print("Sorry, this room is already booked during this period, select another time")
        else:
            myclass.reserve(start, end)

        print(myclass.schedule)


main()
