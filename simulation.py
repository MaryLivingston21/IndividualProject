from Animal import ANIMAL
from Volunteer import VOLUNTEER


class SIMULATION:
    def __init__(self, animal_shelter):
        self.animal_shelter = animal_shelter

    def run(self):
        susan = VOLUNTEER('Susan')
        henry = VOLUNTEER('Henry')
        self.animal_shelter.add_volunteer(susan)
        self.animal_shelter.add_volunteer(henry)

        name_1 = 'Clifford'
        name_2 = 'Killer'
        animal_1 = ANIMAL(name_1, 'Big Red Dog', 5)
        animal_2 = ANIMAL(name_2, 'Golden Labrador', 10)
        self.animal_shelter.add_animal(animal_1)
        self.animal_shelter.add_animal(animal_2)

        volunteer = self.animal_shelter.find_volunteer(1)
        if volunteer is not None:
            animals = self.animal_shelter.find_animal(name_1)
            if len(animals) > 0:
                print(volunteer.to_string() + ' walks ' + animals[0].to_string())
                self.animal_shelter.walk_animal(volunteer, animals[0])
            else:
                print('cannot find animal with name ' + name_1)

            animals = self.animal_shelter.find_animal(name_2)
            if len(animals) > 0:
                print(volunteer.to_string() + ' plays with ' + animals[0].to_string())
                self.animal_shelter.play_w_animal(volunteer, animals[0])
            else:
                print('cannot find animal with name ' + name_2)
        else:
            print('cannot find volunteer with volunteer number 1')

        print('Here are the walks at the Animal Shelter:')
        self.animal_shelter.show_walks()
        print('Here are the play times at the Animal Shelter:')
        self.animal_shelter.show_play_times()

        p = self.animal_shelter.find_volunteer(1)
        if volunteer is not None:
            animals = self.animal_shelter.get_walks(volunteer)
            if len(animals) > 0:
                print(volunteer.to_string() + 'returns ' + animals[0].to_string() + ' from walk \n')
                self.animal_shelter.finish_walk(volunteer, animals[0])
            animals = self.animal_shelter.get_play_times(volunteer)
            if len(animals) > 0:
                print(volunteer.to_string() + ' returns ' + animals[0].to_string() + ' from playtime \n')
                self.animal_shelter.finish_play_time(volunteer, animals[0])
        else:
            print('cannot find volunteer with volunteer number 1')

        print('Here are the walks for the Animal Shelter:')
        self.animal_shelter.show_walks()
        print('Here are the play times at the Animal Shelter:')
        self.animal_shelter.show_play_times()
