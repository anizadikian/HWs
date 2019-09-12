class Classroom:

    classroomIDs = []

    def __init__(self, capacity, roomID):
        self.capacity = capacity
        self.roomID = roomID
        self.schedule = []

    def isFree (self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break
        return is_free

    def Reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @classmethod
    def getAvailableRooms(cls):
        return str.join(",", cls.classroomIDs)

    @staticmethod

    def isValidSlot(start, end):
        return start < end

def main():

    classroom1 = Classroom(60, "212W")
    classroom2 = Classroom(70, "313W")
    classroom3 = Classroom(80, "208E")

    print("Hello, here you can reserve a classroom. Available IDs are: ", Classroom.getAvailableRooms())

    while True:

        print("Please choose number from the following:")
        print("1 : Reserve the room 212W")
        print("2 : Reserve the room 313W")
        print("3 : Reserve the room 208E")

        user_input = int(input())

        if user_input == 1:
            userclassroominput = classroom1
            break
        elif user_input == 2:
            userclassroominput = classroom2
            break
        elif user_input == 3:
            userclassroominput = classroom3
            break
        else:
            print("Please, select 1, 2 or 3")

            while True:

                start = int(input("Please insert the start time of your reservation  "))
                end = int(input("Please insert the end time of your reservation   "))

                    if (Classroom.isValidSlot(start, end)):
                        if userclassroominput.isFree(start, end) == False:
                            print("Sorry, not available for", classroom1.roomID)
                        else:
                            userclassroominput.Reserve(start, end)
                            print("You have reserved the classroom number", classroom1.roomID, "from", start, "to", end)

                            print(userclassroominput.schedule)

                    else:
                        print(userclassroominput.schedule)
main()
