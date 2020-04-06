import unittest

unittest.TestLoader.sortTestMethodsUsing = None

from AnimalShelter import ANIMALSHELTER
from Volunteer import VOLUNTEER
from Animal import ANIMAL


class TestWalk(unittest.TestCase):
    animal_shelter = None

    @classmethod
    def setUpClass(cls):
        # called one time, at beginning
        print('setUpClass()')

        # create shelter
        cls.animal_shelter = ANIMALSHELTER().get()

        # create three animals
        name_1 = 'Charlie'
        name_2 = 'Fido'
        name_3 = 'Sparky'
        breed_a = 'Retriever'
        breed_b = 'German Shepard'
        breed_c = 'Wiener Dog'
        cls.animal1 = ANIMAL(name_1, breed_a, 1)
        cls.animal2 = ANIMAL(name_2, breed_b, 3)
        cls.animal3 = ANIMAL(name_3, breed_c, 2)

        # create two volunteers
        cls.henry = VOLUNTEER('Henry')
        cls.susan = VOLUNTEER('Susan')

        # add animals and volunteers to shelter
        cls.animal_shelter.add_volunteer(cls.henry)
        cls.animal_shelter.add_volunteer(cls.susan)
        cls.animal_shelter.add_animal(cls.animal1)
        cls.animal_shelter.add_animal(cls.animal2)
        cls.animal_shelter.add_animal(cls.animal3)

    @classmethod
    def tearDownClass(cls):
        # called one time, at end
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')

    # -------------------------------------------------------------

    def test_walk_one(self):
        print("TEST1")
        # check that the animal shelter shows that henry is on no walks
        animals = self.animal_shelter.get_walks(self.henry)
        self.assertEqual(len(animals), 0)

        # put henry on a walk
        w = self.animal_shelter.walk_animal(self.henry, self.animal1)

        # check that the animal shelter shows that henry is on a walk w one animal
        animals = self.animal_shelter.get_walks(self.henry)
        self.assertEqual(len(animals), 1)

        # check that the animal on walk with henry is animal1
        if len(animals) == 1:
            self.assertEqual(animals[0], self.animal1)

        # check that henry shows walk with one dog
        animals = self.henry.get_walks()
        self.assertEqual(len(animals), 1)

        # check that the animal on walk with henry is animal1
        if len(animals) == 1:
            self.assertEqual(animals[0], self.animal1)

    # -------------------------------------------------------------

    def test_walk_two(self):
        print("TEST2")
        # susan takes different animal on walk
        w = self.animal_shelter.walk_animal(self.susan, self.animal2)
        self.assertIsNotNone(w)

        # check that the animal shelter shows susan is on a walk with one animal
        animals = self.animal_shelter.get_walks(self.susan)
        self.assertEqual(len(animals), 1)

        # check that the animal on walk with susan is animal2
        if len(animals) == 1:
            self.assertEqual(animals[0], self.animal2)

        # check that susan is on walk with one animal
        animals = self.susan.get_walks()
        self.assertEqual(len(animals), 1)

        # check that the animal on walk with susan is animal2
        if len(animals) == 1:
            self.assertEqual(animals[0], self.animal2)

    # -------------------------------------------------------------

    def test_playTimes(self):
        print("TEST3")
        # susan takes different animal on a playtime
        w = self.animal_shelter.play_w_animal(self.susan, self.animal3)
        self.assertIsNotNone(w)

        # check that the animal shelter shows susan is playing with one animal
        animals = self.animal_shelter.get_play_times(self.susan)
        self.assertEqual(len(animals), 1)

        # check that the animal playing  with susan is animal2
        if len(animals) == 1:
            self.assertEqual(animals[0], self.animal3)

        # check that susan is playing with one animal
        animals = self.susan.get_play_times()
        self.assertEqual(len(animals), 1)

        # check that the animal playing with mary is animal3
        if len(animals) == 1:
            self.assertEqual(animals[0], self.animal3)

    # -------------------------------------------------------------

    def test_z_walk_return(self):
        print("Test Return1")
        # have henry finish walk
        rc = self.animal_shelter.finish_walk(self.henry, self.animal1)
        self.assertTrue(rc)

        # try to return the same animal again--should return False
        rc = self.animal_shelter.finish_walk(self.henry, self.animal1)
        self.assertFalse(rc)

        # check that the animal shelter shows that henry has no walks
        walks = self.animal_shelter.get_walks(self.henry)
        self.assertEqual(len(walks), 0)

        # check that henry has no walks
        walks = self.animal_shelter.get_walks(self.henry)
        self.assertEqual(len(walks), 0)

    # -------------------------------------------------------------

    def test_z_play_time_return(self):
        print("Test Return2")
        # have susan finish playtime
        rc = self.animal_shelter.finish_play_time(self.susan, self.animal3)
        self.assertTrue(rc)

        # try to return the same animal again--should return False
        rc = self.animal_shelter.finish_walk(self.susan, self.animal3)
        self.assertFalse(rc)

        # check that the animal shelter shows that susan has no playtimes
        playtimes = self.animal_shelter.get_play_times(self.susan)
        self.assertEqual(len(playtimes), 0)

        # check that susan has no playtimes
        playtimes = self.animal_shelter.get_play_times(self.susan)
        self.assertEqual(len(playtimes), 0)


# -----------------------------------------

if __name__ == "__main__":
    unittest.main()
