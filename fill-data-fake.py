
from faker import factory,Faker 
from recipes.models import Recipe




from faker import Faker
def populate_data():
    fake = Faker()
    for _ in range(100):
        my_model = Recipe(
            name=fake.name(),
            date=fake.date(),
            difficulty=1,
            timetoprepare=60,
            intro=fake.text(),
            steps=fake.paragraph(),
            outro=fake.paragraph(),

        )
        my_model.save()


if __name__ == '__main__':
    populate_data()
