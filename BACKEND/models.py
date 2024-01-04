from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, VARCHAR, UUID, DATE, SmallInteger, LargeBinary, TEXT
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base
import uuid


class Wine(Base):
    __tablename__ = 'wines'
    
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid1)
    name = Column(VARCHAR, nullable=False)
    harvest = Column(VARCHAR, nullable=False)
    winery = Column(VARCHAR, nullable=False)
    cover = Column(VARCHAR, nullable=False)
    grapes= Column(VARCHAR, nullable=False)
    production_area = Column(VARCHAR, nullable=False)
    type_of_land = Column(VARCHAR, nullable=False)
    breeding_system = Column(VARCHAR, nullable=False)
    fermentation = Column(VARCHAR, nullable=False)
    refinement = Column(VARCHAR, nullable=False)
    months_of_refinement = Column(VARCHAR, nullable=False)
    alcohol_content = Column(VARCHAR, nullable=False)
    total_acidity = Column(VARCHAR, nullable=False)
    residual_sugars = Column(VARCHAR, nullable=False)
    first_year_of_production = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=False)
    refinement_bottle = Column(VARCHAR, nullable=False)
    image = Column(LargeBinary)
    link_site = Column(VARCHAR, nullable=False)
    link_ecommerce = Column(VARCHAR)
    decanting_time = Column(VARCHAR)
    video = Column(VARCHAR)


class User(Base):
    __tablename__ = 'accounts'
    
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid1)
    email = Column(VARCHAR, nullable=False)
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)
    birth_date = Column(DATE)
    type = Column(SmallInteger)
    password = Column(VARCHAR, nullable=False)
    apple_user = Column(VARCHAR)