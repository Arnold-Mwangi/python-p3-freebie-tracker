from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

##Association tables
dev_freebies = Table('dev_freebies', Base.metadata,
    Column('dev_id', Integer(), ForeignKey('devs.id')),
    Column('freebie_id', Integer(), ForeignKey('freebies.id'))
)


dev_companies = Table('dev_companies', Base.metadata,
    Column('dev_id', Integer, ForeignKey('devs.id')),
    Column('company_id', Integer, ForeignKey('companies.id'))
)




class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    devs = relationship('Dev', secondary='dev_companies', backref='companies')

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value):
        # Create a new Freebie instance associated with this company and the given dev.
        freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        session.add(freebie)
        session.commit()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'

    freebies = relationship('Freebie', secondary='dev_freebies', backref = 'devs')

    def received_one(self, item_name):
        # Check if any of the freebies associated with the dev has the specified item_name.
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        # Ensure that the freebie belongs to the dev who's giving it away.
        if freebie.dev == self:
            freebie.dev = other_dev
            session.commit()

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name= Column(String())
    value=Column(Integer())
    company_id=Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    def __repr__(self):
        return f'<Freebie {self.item_name}, {self.value}>'

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'