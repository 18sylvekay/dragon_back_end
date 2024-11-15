import kronos

from project.dragons.models import Dragon


@kronos.register("0 * * * *")
def deplete_food_and_happiness():
    dragons = Dragon.objects.all()
    for dragon in dragons:
        if dragon.food_percentage > 0:
            dragon.food_percentage -= 10

        if dragon.happiness_rating > 0:
            dragon.happiness_rating -= 5
        dragon.save()
