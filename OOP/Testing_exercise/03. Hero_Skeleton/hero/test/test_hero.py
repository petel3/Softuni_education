from unittest import TestCase,main

from project.hero import Hero


class testHero(TestCase):
    def setUp(self):
        self.hero=Hero("Username", 6 ,70.00 ,50.00)
    def test_init_creates_all_atributes(self):
        self.hero.username="Pesho"
        self.hero.level=9
        self.hero.health=80.00
        self.hero.damage=55.00
        self.assertEqual("Pesho",self.hero.username)
        self.assertEqual(9,self.hero.level)
        self.assertEqual(80.00,self.hero.health)
        self.assertEqual(55.00,self.hero.damage)

    def test_battle_method_raise_exeption_if_other_hero_has_same_name(self):
        self.other_hero = Hero("Username", 3, 3.00, 40.00)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.other_hero)
        self.assertEqual("You cannot fight yourself",str(ex.exception))

    def test_battle_method_is_main_hero_not_enough_health(self):
        self.hero.health=0
        self.other_hero = Hero("Gosho", 3, 3.00, 40.00)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.other_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

    def test_battle_method_is_other_hero_not_enough_health(self):
        self.other_hero = Hero("Gosho", 3, 0, 40.00)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.other_hero)
        self.assertEqual(f"You cannot fight {self.other_hero.username}. He needs to rest",str(ex.exception))

    def test_battle_method_is_draw_case(self):
        self.other_hero=Hero("Gosho", 3, 40, 40.00)
        self.hero=Hero("Username", 3, 40, 40.00)
        expected="Draw"
        self.assertEqual(expected,self.hero.battle(self.other_hero))

    def test_battle_method_is_main_hero_beat_other_hero(self):
        self.other_hero = Hero("Gosho", 1, 40, 40.00)
        self.hero = Hero("Username", 1, 90, 40.00)
        expect="You win"

        self.assertEqual(expect,self.hero.battle(self.other_hero))
        self.assertEqual(2,self.hero.level)
        self.assertEqual(45.00,self.hero.damage)
        self.assertEqual(55,self.hero.health)

    def test_battle_method_is_other_hero_beat_main_hero(self):
        self.hero = Hero("Gosho", 1, 40, 40.00)
        self.other_hero = Hero("Username", 1, 90, 40.00)
        expect = "You lose"

        self.assertEqual(expect, self.hero.battle(self.other_hero))
        self.assertEqual(2, self.other_hero.level)
        self.assertEqual(45.00, self.other_hero.damage)
        self.assertEqual(55, self.other_hero.health)

    def test_hero_info_returned_in_string(self):


        result=f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(result,str(self.hero))
if __name__=="__main__":
    main