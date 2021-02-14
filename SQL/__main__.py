# coding=utf-8

from .car import Car
from .brand import Brand
from ..common.base import session_factory


def populate_database():
    session = session_factory()

    audiA3 = Car("A3",110, 1, 2020)
    mercedesC = Car("Clase C",140, 2, 2020)
    peugeot3008 = Car("3008",120, 2, 2020)
    bmwX1 = Car("X1",140, 3, 2020)
    astra = Car("Astra",110, 3, 2020)
    audiA5 = Car("A5",180, 1, 2020)

    audi = Brand("Audi", [audiA3, audiA5])
    mercedes = Brand("Mercedes", [mercedesC])
    peugeot = Brand("Peugeot", [peugeot3008])
    opel = Brand("Opel", [astra])
    bmw = Brand("BMW", [bmwX1])

    session.add(audi)
    session.add(mercedes)
    session.add(peugeot)
    session.add(opel)
    session.add(bmw)

    session.commit()
    session.close()


def query_courses():
    session = session_factory()
    course_query = session.query(Car)
    session.close()
    return course_query.all()


if __name__ == "__main__":
    brands = query_courses()
    if len(brands) == 0:
        populate_database()

        brands = query_courses()
    for brand in brands:
        print(f'"{brand.name}" has the following models: ', end="")

        for student in brand.cars:
            print(f'{car.model}; ', end="")

        print('')
