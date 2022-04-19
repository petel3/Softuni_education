from project.team import Team
from unittest import TestCase,main
class Test(TestCase):
    def setUp(self) -> None:
        self.team=Team("Pesho")
        self.other=Team("Vasko")

    def test_initialization_should_raise_error_for_name(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name="1petur"
        self.assertEqual("Team Name can contain only letters!",str(ex.exception))

    def test_initialization_shoud_be_correct(self):
        self.assertEqual("Pesho",self.team.name)
        self.assertEqual({}, self.team.members)
        self.team.members={"Andi":10}
        self.assertEqual({"Andi":10},self.team.members)

    def test_add_members(self):
        player={
            "Andi":10,
            "Pesho": 20,
            "Kiro":30
                }
        self.assertEqual(f"Successfully added: Andi, Pesho, Kiro",self.team.add_member(**player))
        self.team.add_member(**player)
        self.assertEqual({
            "Andi":10,
            "Pesho": 20,
            "Kiro":30
                },self.team.members)
        self.assertTrue(self.team.add_member(**player))

    def test_remove_players_from_team_when_exist(self):
        self.team.members = {"Andi": 10}
        self.assertEqual(1, len(self.team.members))
        self.assertEqual(f"Member Andi removed",self.team.remove_member("Andi"))

        self.team.remove_member("Andi")
        self.assertEqual(0,len(self.team.members))

    def test_remove_players_from_team_when_dont_exist_case(self):
        self.team.members = {"Andi": 10}
        self.assertEqual(f"Member with name Pesho does not exist", self.team.remove_member("Pesho"))
        self.team.remove_member("Pesho")
        self.assertEqual(1, len(self.team.members))

    def test_gt_overriding_method(self):
        team1=Team("First")
        team2=Team("Second")
        team2.members = {"Andi": 10}
        x=team1<team2
        y=team1>team2


        self.assertEqual(False,y)
        self.assertEqual(True,x)



    def test_len_overriding_method(self):
        self.team.members = {"Andi": 10,"Gosho": 10}
        self.assertEqual(2,self.team.__len__())
        self.assertEqual(2,len(self.team))

    def test_add_name_overriding_method(self):
        self.team.members = {"Andi": 10}
        self.other.members = {"Gosho": 10}
        expected = f"Team name: PeshoVasko\n" + f"Member: Andi - 10-years old\n" + f"Member: Gosho - 10-years old"
        self.assertEqual(expected,self.team.__add__(self.other).__str__())

        self.assertEqual(2,len(self.team.__add__(self.other).members))
        self.assertEqual("PeshoVasko", self.team.__add__(self.other).name)
        self.assertIsInstance(self.team.__add__(self.other),Team)



    def test_str_overriding_method(self):

        self.team.members = {"Test": 10, "sTest": 20}

        self.assertEqual(f"Team name: Pesho\n" 
                         f"Member: sTest - 20-years old\n"
                         f"Member: Test - 10-years old",str(self.team))
if __name__=="__main__":
    main