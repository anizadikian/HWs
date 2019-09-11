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
        return is_Free

    def reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False


def main():

    while True:
        print("Please choose number from the following:")
        print("1 : Reserve a new classroom")
        print("2 : Exit the reservation application")

        user_input = int(input())

        if user_input == 1:

            classroom1 = Classroom(30, "212W")

            while True:

                start = int(input("Please insert the start time of your reservation  "))
                end = int(input("Please insert the end time of your reservation   "))

                if classroom1.isFree(start, end) == False:
                    print("Sorry, the rooom", classroom1.nclassrom, "is already booked during this period, select another time or classroom")
                else:
                    classroom1.reserve(start, end)

                print("You have reserved the classroom number", classroom1.nclassrom, "during the period", classroom1.schedule)
        else:
            print("Thanks for using the application")
            exit()
main()
