from project.dragons.models import Dragon

dragons = Dragon.objects.all()
for dragon in dragons:
    if dragon.food_percentage > 0:
        dragon.food_percentage -= 40

    if dragon.happiness_rating > 0:
        dragon.happiness_rating -= 40
    dragon.save()
