import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.CreateDB import *
import Functions.GetData as GD
import Functions.ParseInfo as PI

# Conexión a la base de datos
engine = create_engine("postgresql://postgres:alex2134@localhost:5432/neuroapp")
Session = sessionmaker(bind=engine)
session = Session()


def fetch_and_store_data(fitness):
    Time = dt.datetime.now()
    yesterday = Time - dt.timedelta(days=1)
    StarTime = dt.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
    EndTime = dt.datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 0)

    heart_rate_data = GD.GetDatasetHearRate(StarTime, EndTime, "me", fitness)
    parse_heart_rate_data = PI.parse_heart_bpm(heart_rate_data, "Heart Rate")

    for data_point in parse_heart_rate_data["Heart Rate"]:
        heart_rate_entry = HeartRate(
            av_ppm=data_point["Av_ppm"],
            max_ppm=data_point["Max_ppm"],
            min_ppm=data_point["Min_ppm"],
            time_recorded=data_point["Date"],
        )

        session.add(heart_rate_entry)

    session.commit()
    print("Heart Rate data stored")
