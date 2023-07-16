from modelle.CookedDish import CookedDish
from repository.CookedDishRepo import CookedDishRepo
from repository.DrinkRepo import DrinkRepo


# 1. Hinzufügen eines dishs

def test_add_dish():
    repo = CookedDishRepo("dishes.csv")
    dish1 = CookedDish("1", "Savarina", "10", "20", "350")
    Liste = [dish1]
    repo.save(Liste)
    dish = repo.load()[-1]

    try:
        assert dish1 == dish
        print("gut")
    except:
        print("schlecht")


def test_add_beverage():
    from modelle.Beverage import Beverage
    repo = DrinkRepo("beverages.csv")
    getrank1 = Beverage("1", "mata", "2", "67", "350")
    Liste = [getrank1]
    repo.save(Liste)
    Beverage = repo.load()[-1]

    assert getrank1 == Beverage



