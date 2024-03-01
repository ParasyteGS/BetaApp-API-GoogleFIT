from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    Date,
    Time,
    DateTime,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine("postgresql://postgres:alex2134@localhost:5432/neuroapp")

Base = declarative_base()


class Paciente(Base):
    __tablename__ = "Pacientes"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    gender = Column(String(100))
    email = Column(String(100))
    height = Column(Float)
    phone_number = Column(Integer)
    access_token = Column(Text)
    refresh_token = Column(Text)


class DailyData(Base):
    __tablename__ = "DailyData"
    daily_data_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Pacientes.user_id"))
    date = Column(Date)
    paciente = relationship("Paciente")


class MinuteData(Base):
    __tablename__ = "MinuteData"
    minute_data_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Pacientes.user_id"))
    date = Column(Date)
    paciente = relationship("Paciente")


class HeartRate(Base):
    __tablename__ = "HeartRate"
    heart_rate_id = Column(Integer, primary_key=True)
    minute_data_id = Column(Integer, ForeignKey("MinuteData.minute_data_id"))
    av_ppm = Column(Integer)
    max_ppm = Column(Integer)
    min_ppm = Column(Integer)
    time_recorded = Column(Time)
    minute_data = relationship("MinuteData")


class ActivityType(Base):
    __tablename__ = "ActivityType"
    activity_type_id = Column(Integer, primary_key=True)
    minute_data_id = Column(Integer, ForeignKey("MinuteData.minute_data_id"))
    type_activity = Column(String(100))
    time_recorded = Column(Time)
    minute_data = relationship("MinuteData")


class ActivityDaily(Base):
    __tablename__ = "ActivityDaily"
    activity_daily_id = Column(Integer, primary_key=True)
    daily_data_id = Column(Integer, ForeignKey("DailyData.daily_data_id"))
    activity_minutes = Column(Integer)
    daily_data = relationship("DailyData")


class BloodPressure(Base):
    __tablename__ = "BloodPressure"
    blood_pressure_id = Column(Integer, primary_key=True)
    minute_data_id = Column(Integer, ForeignKey("MinuteData.minute_data_id"))
    sis_av = Column(Float)
    sis_min = Column(Float)
    sis_max = Column(Float)
    dia_av = Column(Float)
    dia_min = Column(Float)
    dia_max = Column(Float)
    time_recorded = Column(Time)
    minute_data = relationship("MinuteData")


class BodyFat(Base):
    __tablename__ = "BodyFat"
    body_fat_id = Column(Integer, primary_key=True)
    daily_data_id = Column(Integer, ForeignKey("DailyData.daily_data_id"))
    body_fat_pc = Column(Float)
    daily_data = relationship("DailyData")


class Oxygen(Base):
    __tablename__ = "Oxygen"
    oxygen_id = Column(Integer, primary_key=True)
    minute_data_id = Column(Integer, ForeignKey("MinuteData.minute_data_id"))
    av_pc = Column(Float)
    max_pc = Column(Float)
    min_pc = Column(Float)
    time_recorded = Column(Time)
    minute_data = relationship("MinuteData")


class Weight(Base):
    __tablename__ = "Weight"
    weight_id = Column(Integer, primary_key=True)
    daily_data_id = Column(Integer, ForeignKey("DailyData.daily_data_id"))
    weight = Column(Float)
    daily_data = relationship("DailyData")


class Calories(Base):
    __tablename__ = "Calories"
    calories_id = Column(Integer, primary_key=True)
    daily_data_id = Column(Integer, ForeignKey("DailyData.daily_data_id"))
    calories = Column(Float)
    daily_data = relationship("DailyData")


class Sleep(Base):
    __tablename__ = "Sleep"
    sleep_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Pacientes.user_id"))
    sleep_type = Column(String(100))
    time_recorded = Column(DateTime)
    paciente = relationship("Paciente")


Base.metadata.create_all(engine)
