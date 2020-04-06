from Walk import WALK
from PlayTime import PLAYTIME


class ANIMALSHELTER:
    s_animal_shelter = None

    @classmethod
    def get(self):
        if self.s_animal_shelter is None:
            self.s_animal_shelter = ANIMALSHELTER()
        return self.s_animal_shelter

    def __init__(self):
        self.animals = set()
        self.volunteers = set()
        self.walks = set()
        self.play_times = set()

    def add_volunteer(self, volunteer):
        self.volunteers.add(volunteer)

    # def remove_volunteer(self, volunteer):
    #     if volunteer in self.volunteers:
    #         self.volunteers.remove(volunteer)

    def get_volunteers(self):
        return self.volunteers

    def find_volunteer(self, volunteer_number):
        for volunteer in self.volunteers:
            if volunteer.get_volunteer_number() == volunteer_number:
                return volunteer
        return None

    def add_animal(self, animal):
        self.animals.add(animal)

    # def remove_animal(self, animal):
    #     if animal in self.animals:
    #         self.animals.remove(animal)

    def get_animals(self):
        return self.animals

    def find_animal(self, name):
        animals = []
        for animal in self.animals:
            if animal.get_name() == name:
                animals.append(animal)
        return animals

    def walk_animal(self, volunteer, animal):
        if not self.is_on_walk(animal):
            w = WALK(volunteer, animal)
            self.walks.add(w)
            volunteer.walk_animal(animal)
            return w
        else:
            return None

    def is_on_walk(self, animal):
        for w in self.walks:
            if w.get_animal() == animal:
                return True
        return False

    def play_w_animal(self, volunteer, animal):
        if not self.is_playing(animal):
            p = PLAYTIME(volunteer, animal)
            self.play_times.add(p)
            volunteer.play_w_animal(animal)
            return p
        else:
            return None

    def is_playing(self, animal):
        for p in self.play_times:
            if p.get_animal() == animal:
                return True
        return False

    def show_walks(self):
        for w in self.walks:
            print(w.get_volunteer().to_string() + ' => ' + w.get_animal().to_string())

    def get_walks(self, volunteer):
        walk_list = []
        for w in self.walks:
            if w.get_volunteer() == volunteer:
                walk_list.append(w.get_animal())
        return walk_list

    def show_play_times(self):
        for p in self.play_times:
            print(p.get_volunteer().to_string() + ' => ' + p.get_animal().to_string())

    def get_play_times(self, volunteer):
        play_time_list = []
        for p in self.play_times:
            if p.get_volunteer() == volunteer:
                play_time_list.append(p.get_animal())
        return play_time_list

    def finish_walk(self, volunteer, animal):
        self.show_walks()
        #print("V: " + volunteer.to_string())
        #print("A: " + animal.to_string())
        for w in self.walks:
            if w.get_volunteer() == volunteer and w.get_animal() == animal:
                self.walks.remove(w)
                return True
        return False

    def finish_play_time(self, volunteer, animal):
        for w in self.play_times:
            if w.get_volunteer() == volunteer and w.get_animal() == animal:
                self.play_times.remove(w)
                return True
        return False
