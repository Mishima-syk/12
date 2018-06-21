import os
from sqlalchemy import *
from sqlalchemy.orm import create_session, relationship
from sqlalchemy.ext.declarative import declarative_base

uri = 'sqlite:///CHEMBL930273.db'

Base = declarative_base()
engine = create_engine(uri)
metadata = MetaData(bind=engine)


class Compound(Base):
    __table__ = Table('compound', metadata, autoload=True)


class Property(Base):
    __table__ = Table('property_name', metadata, autoload=True)


class CompoundProperty(Base):
    __table__ = Table('compound_property', metadata, autoload=True)
    compound = relationship('Compound', backref='compound_properties')
    property = relationship('Property', backref='compound_properties')


class RuleEnvironment(Base):
    __table__ = Table('rule_environment', metadata, autoload=True)


class ConstantSmiles(Base):
    __table__ = Table('constant_smiles', metadata, autoload=True)


class Pair(Base):
    __table__ = Table('pair', metadata, autoload=True)
    constant_smiles = relationship('ConstantSmiles', backref='pair')
    rule_environment = relationship('RuleEnvironment', backref='pair')


mmpdb = create_session(bind=engine)
