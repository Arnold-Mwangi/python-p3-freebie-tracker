from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Create an SQLite database (you can replace 'sqlite:///your_database.db' with your preferred database URL).
engine = create_engine('sqlite:///freebies.db')

# Create the tables in the database.
Base.metadata.create_all(engine)

# Create a session to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data (replace this with your actual data population logic).
company1 = Company(name='Company A', founding_year=2000)
company2 = Company(name='Company B', founding_year=2010)

dev1 = Dev(name='Dev 1')
dev2 = Dev(name='Dev 2')

# Add the objects to the session and commit them to the database.
session.add_all([company1, company2, dev1, dev2])
session.commit()

# Create freebies with company and dev relationships based on your structure.
freebie1 = Freebie(item_name='Item 1', value=100, company_id=company1.id, dev_id=dev1.id)
freebie2 = Freebie(item_name='Item 2', value=50, company_id=company2.id, dev_id=dev1.id)
freebie3 = Freebie(item_name='Item 3', value=75, company_id=company1.id, dev_id=dev2.id)

# Add the freebies to the session and commit them to the database.
session.add_all([freebie1, freebie2, freebie3])
session.commit()

# Now you can test the methods you mentioned:

# Get all freebies for a company.
company1_freebies = session.query(Freebie).filter_by(company_id=company1.id).all()
print("Company 1 Freebies:", company1_freebies)

# Get all devs who collected freebies from a company.
company1_devs = session.query(Dev).filter(Dev.freebies.any(company_id=company1.id)).all()
print("Devs from Company 1:", company1_devs)

# Get all freebies collected by a dev.
dev1_freebies = session.query(Freebie).filter_by(dev_id=dev1.id).all()
print("Dev 1 Freebies:", dev1_freebies)

# Get all companies that a dev has collected freebies from.
dev1_companies = session.query(Company).filter(Company.devs.any(id=dev1.id)).all()
print("Companies for Dev 1:", dev1_companies)
