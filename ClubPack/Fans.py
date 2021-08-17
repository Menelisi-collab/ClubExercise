# Module

class Fans:
    def __init__(self, first_name, last_name, status):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status

    def move(self):
        print("Getting into Stadium...")

    def cheer(self):
        print("Cheering and chantign songs..")

    def jeer(self):
        print("Jeering and chanting slurs")

    def leave(self):
        print("Leaving the Stadium...")
