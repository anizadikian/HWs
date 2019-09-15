class Room:

    room = {}

    def __init__(self, capacity, roomID):
        self.capacity = capacity
        self.roomID = roomID
        self.schedule = []
        Room.room[roomID] = self
        print(Room.room)

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
    def getAvailableRooms(cls):
        ids = []
        for key in cls.room:
            ids.append(key)
        return str.join(",", ids)

    @classmethod
    def getRoomById(cls, ID):
        if ID in cls.room.keys():
            return cls.room[ID]
        print("the room cannot be found")
        return False

    @classmethod
    def printCurrentStateofAllRooms(cls):
        for key in cls.room:
            currRoom = cls.room[key]
            print(currRoom.roomID)
            print("Capacity: ", currRoom.capacity)
            print("Schedule: ", currRoom.schedule)

    @staticmethod
    def isValidSlot(start, end):
        return start < end

class Office(Room):
    def __init__(self, roomID, instructor):
        pass

class Classroom(Room):
    def __init__(self,roomID,capacity):
        pass

def mainClassroom():
    Classroom( "313E PAB", 100)
    Classroom( "314W PAB", 30)
    Classroom( "315W PAB", 65)
    Classroom( "316E PAB", 70)

    print("Hello, here you can reserve a classroom. Available IDs are:\n", Room.getAvailableRooms())

    while True:

        classroomID = input("Please select a room ID from above")
        currClassroom = Classroom.getRoomById(classroomID)
        if currClassroom == False:
            break
        start = int(input("Please insert the starting time"))
        end = int(input("Please insert the ending time"))

        if (Classroom.isValidSlot(start, end)):
            if currClassroom.isFree(start, end) == False:
                print("Not available for ", currClassroom.roomID)
            else:
                currClassroom.Reserve(start, end)
                print("You just reserved the classroom", currClassroom.roomID, " from ", start, " to ", end)

                print(currClassroom.schedule)
        else:
            print("The slot is invalid")

mainClassroom()

def mainOffice:

mainOffice()

def main
    
main()

