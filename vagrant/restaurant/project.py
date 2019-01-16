from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, Menu_Item
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker (bind = engine)
session = DBSession()

# newEntry = ClassName(property = "value",...)
# session.add(newEntry)
# session.commit()

# myFirstRestaurant = Restaurant(name = "Pizza Palace")
# session.add(myFirstRestaurant)
# session.commit()
#
# print(session.query(Restaurant).all())
#
# cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella",
# course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
# session.add(cheesepizza)
# session.commit()
#
# print(session.query(MenuItem).all())
#
# firstResult = session.query(Restaurant).first()
# print(firstResult.name )

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
    UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
    print UrbanVeggieBurger.price $5.99
    UrbanVeggieBurger.price = '$2.99'
    session.add(UrbanVeggieBurger)
    session.commit()
    veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
    for veggieBurger in veggieBurgers:
         print veggieBurger.id
         print veggieBurger.price
         print veggieBurger.restaurant.name
        print "\n"
    for veggieBurger in veggieBurgers:
        if veggieBurger.price != '$2.99':
            veggieBurger.price = '$2.99'
            session.add(veggieBurger)
            session.commmit()

    for veggieBurger in veggieBurgers:
        print veggieBurger.id
        print veggieBurger.price
        print veggieBurger.restaurant.name
        print "\n"

    spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
        pint spinach.restaurant.name
        Auntie Ann's Diner
            session.delete(spinach)
            session.commit() 
