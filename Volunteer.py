from Walk import WALK
from PlayTime import PLAYTIME


class VOLUNTEER:
    s_next_volunteer_number = 0

    def __init__(self, name):
        self.name = name
        VOLUNTEER.s_next_volunteer_number = VOLUNTEER.s_next_volunteer_number + 1
        self.volunteer_number = VOLUNTEER.s_next_volunteer_number
        self.walks = set()
        self.play_times = set()

    def to_string(self):
        return self.name + ': volunteer number = ' + str(self.volunteer_number) + '  number of walk(s) = ' + \
               str(len(self.walks)) + ';  number of playtime(s) = ' + \
               str(len(self.play_times)) + '\n'

    def get_volunteer_number(self):
        return self.volunteer_number

    def get_name(self):
        return self.name

    def get_walks(self):
        return list(self.walks)

    def get_play_times(self):
        return list(self.play_times)

    def __eq__(self, other):
        return self.name == other.name and self.volunteer_number == other.volunteer_number

    def __hash__(self):
        return hash((self.name, self.volunteer_number))

    def walk_animal(self, animal):
        self.walks.add(animal)

    def play_w_animal(self, animal):
        self.play_times.add(animal)
