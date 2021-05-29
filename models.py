import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, DECIMAL, create_engine
from sqlalchemy.orm import declarative_base, session, sessionmaker

load_dotenv()

con_string = os.environ.get('DB_CON_STRING')

engine = create_engine(con_string, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Ethereum(Base):
    __tablename__ = 'ethereum'

    id = Column(Integer(), primary_key=True)
    ask = Column(DECIMAL(15, 5))
    bid = Column(DECIMAL(15, 5))
    last = Column(DECIMAL(15, 5))
    open = Column(DECIMAL(15, 5))
    low = Column(DECIMAL(15, 5))
    high = Column(DECIMAL(15, 5))
    volume = Column(DECIMAL(15, 8))
    date_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return ('Ethereum('
                f'id: {self.id}, '
                f'ask: {self.ask}, '
                f'bid: {self.bid}, '
                f'last: {self.last}, '
                f'open: {self.open}, '
                f'low: {self.low}, '
                f'high: {self.high}, '
                f'volume: {self.volume}, '
                f'timestamp: {self.date_time})'
                )


class Polygon(Base):
    __tablename__ = 'polygon'

    id = Column(Integer(), primary_key=True)
    ask = Column(DECIMAL(15, 5))
    bid = Column(DECIMAL(15, 5))
    last = Column(DECIMAL(15, 5))
    open = Column(DECIMAL(15, 5))
    low = Column(DECIMAL(15, 5))
    high = Column(DECIMAL(15, 5))
    volume = Column(DECIMAL(15, 8))
    date_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return ('Polygon('
                f'id: {self.id}, '
                f'ask: {self.ask}, '
                f'bid: {self.bid}, '
                f'last: {self.last}, '
                f'open: {self.open}, '
                f'low: {self.low}, '
                f'high: {self.high}, '
                f'volume: {self.volume}, '
                f'timestamp: {self.date_time})'
                )
