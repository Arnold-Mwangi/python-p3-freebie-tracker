#!/usr/bin/env python3

# Script goes here!
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Freebie, Dev, Company


engine=create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session=Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

fake = Faker()

freebies =[]
for i in range(50):
    freebie=Freebie(
        item_name =fake.unique.name(),
        value=fake.random_int(min=1, max=50)

    )
    session.add(freebie)
    freebies.append(freebie)
session.commit()
session.close()
        
    