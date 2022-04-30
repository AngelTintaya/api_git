from application import db
from application import Drink

# Creating the database
db.create_all()

drink = Drink(name="Grape Soda", description="Tastes like grapes")
# drink  # To see results

# Adding to the table:
db.session.add(drink)
db.session.commit()

# Drink.query.all()  # To identify all data from Drink table

# Adding other dring
db.session.add(Drink(name="Cherry", description="Tasted kike that one ice cream"))
db.session.commit()

# Drink.query.all()  # To identify all data from Drink table

