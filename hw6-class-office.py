class Room:

    rooms = []

    def __init__(self, type, ID, capacity):
        self.type = type
        self.ID = ID
        self.capacity = capacity
        Room.rooms.append(self)

    def print(self):
        print("This room", self.ID, self.type)

    @classmethod
    def getRooms(cls):
        for room in cls.rooms:
            room.print()

    @classmethod
    def getRoombytype(cls, type):
        for room in cls.rooms:
            if room.type == type:
                room.print()

    @classmethod
    def getAvailableClassRooms(cls):
        ids = []
        for key in cls.rooms:
         ids.append(key)
        return str.join(",", ids)

    @classmethod
    def getRoomById(cls, ID):
        if ID in cls.rooms.keys():
            return cls.rooms[ID]
        print("Invalid room")
        return False


class Classroom(Room):

    type = "classroom"
    classrooms = {}

    def __init__(self, ID, capacity):
        super().__init__(Classroom.type, ID, capacity)
        self.schedule = []

    def isFree(self, start, end):
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
        def getscheduleofAllClsRooms(cls):
            for key in cls.rooms:
                currRoom = cls.rooms[key]
                print(currRoom.roomID, ' :')
                print("capacity: ", currRoom.capacity)
                print("schedule: ", currRoom.schedule)

class Office(Room):
    type = "office"

    def __init__(self, ID, capacity):
        super().__init__(Office.type, ID, capacity)
        self.faculty = []

    def facultyMembers(self):
        while True:
            member = input("Type faculty members")
            if member not in Room.getRoomsByType("Office"):
                self.faculty.append(member)
            else:
                print("The member is already in the list")

def main():

    ClassRoom("313E", 50)
    ClassRoom("310W PAB", 100)

    Office("110E PAB", 3)
    Office("106E PAB", 4)
    Office("107E PAB", 1)

    Office.getAvailableRooms(), "These rooms are classrooms:",
    Room.getRoomsByType("Classroom"), "and these are offices:", Room.getRoomsByType("office"))

    while True:

        ID = input("Dear user please choose an ID from above.")
        Room = Room.getRoomById(ID)

        if ID == Room.getRoomsByType("Classroom"):
            start = int(input("input the starting time"))
            end = int(input("input the ending time"))

            if (Classroom.isValidSlot(start, end)):
                if Room.isFree(start, end) == False:
                    print("Not available for ", ID.roomID)
                else:
                    currClassroom.Reserve(start, end)
                    print("You just reserved the classroom", ID.roomID, " from ", start, " to ", end)

                    print(ID.schedule)

            else:
                print("The slot is invalid")

        elif ID == Room.getRoomsByType("Office"):
            print(Office.facultyMembers())


        else:
            print("Chose the room wrong")

main()
