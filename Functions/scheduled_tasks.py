import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.CreateDB import *
import Functions.GetData as GD
import Functions.ParseInfo as PI

# Conexión a la base de datos
engine = create_engine("postgresql://postgres:alex2134@localhost:5432/neurohdb")
Session = sessionmaker(bind=engine)
session = Session()

Time = dt.datetime.now()
yesterday = Time - dt.timedelta(days=1)
yesterday_without_time = dt.datetime(yesterday.year, yesterday.month, 1)
StarTime = dt.datetime(yesterday.year, yesterday.month, 1, 0, 0, 0)
EndTime = dt.datetime(yesterday.year, yesterday.month, 1, 23, 59, 0)


def inser_heart_rate(user_id, fitness):

    heart_rate_data = GD.GetDatasetHearRate(StarTime, EndTime, "me", fitness)
    parse_heart_rate_data = PI.parse_heart_bpm(heart_rate_data, "Heart Rate")

    minute_data = (
        session.query(MinuteData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )
    if not minute_data:
        minute_data = MinuteData(user_id=user_id, date=yesterday_without_time)
        session.add(minute_data)
        session.flush()
        minute_data_id = minute_data.minute_data_id
    else:
        minute_data_id = minute_data.minute_data_id

    for data_point in parse_heart_rate_data["Heart Rate"]:
        new_heart_rate = HeartRate(
            minute_data_id=minute_data_id,
            av_ppm=data_point["Av_ppm"],
            max_ppm=data_point["Max_ppm"],
            min_ppm=data_point["Min_ppm"],
            time_recorded=data_point["Date"],
        )
        session.add(new_heart_rate)
    session.commit()


def insert_oxygen(user_id, fitness):

    oxygen_data = GD.GetDatasetOxSaturation(StarTime, EndTime, "me", fitness)
    parse_oxygen_data = PI.parse_ox_saturation(oxygen_data, "Oxygen Saturation")

    minute_data = (
        session.query(MinuteData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not minute_data:
        minute_data = MinuteData(user_id=user_id, date=yesterday_without_time)
        session.add(minute_data)
        session.flush()
        minute_data_id = minute_data.minute_data_id
    else:
        minute_data_id = minute_data.minute_data_id

    for data_point in parse_oxygen_data["Oxygen Saturation"]:
        new_oxygen = Oxygen(
            minute_data_id=minute_data_id,
            av_pc=data_point["AvPc"],
            max_pc=data_point["MaxPc"],
            min_pc=data_point["MinPc"],
            time_recorded=data_point["Date"],
        )
        session.add(new_oxygen)
    session.commit()


def insert_blood_pressure(user_id, fitness):

    blood_pressure_data = GD.GetDatasetBloodPressure(StarTime, EndTime, "me", fitness)
    parse_blood_pressure_data = PI.parse_blood_pressure(
        blood_pressure_data, "Blood Pressure"
    )

    minute_data = (
        session.query(MinuteData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not minute_data:
        minute_data = MinuteData(user_id=user_id, date=yesterday_without_time)
        session.add(minute_data)
        session.flush()
        minute_data_id = minute_data.minute_data_id
    else:
        minute_data_id = minute_data.minute_data_id

    for data_point in parse_blood_pressure_data["Blood Pressure"]:
        new_blood_pressure = BloodPressure(
            minute_data_id=minute_data_id,
            sis_av=data_point["SisAv"],
            sis_min=data_point["SisMin"],
            sis_max=data_point["SisMax"],
            dia_av=data_point["DiaAv"],
            dia_min=data_point["DiaMin"],
            dia_max=data_point["DiaMax"],
            time_recorded=data_point["Date"],
        )
        session.add(new_blood_pressure)


def inser_activity_type(user_id, fitness):

    activity_data = GD.GetDatasetActivity(StarTime, EndTime, "me", fitness)
    parse_activity_data = PI.parse_activity(activity_data, "Activity Type")

    minute_data = (
        session.query(MinuteData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not minute_data:
        minute_data = MinuteData(user_id=user_id, date=yesterday_without_time)
        session.add(minute_data)
        session.flush()
        minute_data_id = minute_data.minute_data_id
    else:
        minute_data_id = minute_data.minute_data_id

    for data_point in parse_activity_data["Activity Type"]:
        new_activity_type = ActivityType(
            minute_data_id=minute_data_id,
            type_activity=data_point["Type Activity"],
            time_recorded=data_point["Date"],
        )
        session.add(new_activity_type)
    session.commit()


# DailyData


def insert_activity_minutes(user_id, fitness):

    activity_minutes_data = GD.GetDatasetActivityMinutes(
        StarTime, EndTime, "me", fitness
    )
    parse_activity_minutes_data = PI.parse_activity_minutes(
        activity_minutes_data, "Activity Minutes"
    )

    daily_data = (
        session.query(DailyData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not daily_data:
        daily_data = DailyData(user_id=user_id, date=yesterday_without_time)
        session.add(daily_data)
        session.flush()
        daily_data_id = daily_data.daily_data_id
    else:
        daily_data_id = daily_data.daily_data_id

    for data_point in parse_activity_minutes_data["Activity Minutes"]:
        new_activity_minutes = ActivityDaily(
            daily_data_id=daily_data_id,
            activity_minutes=data_point["Activity_minutes"],
        )
        session.add(new_activity_minutes)
    session.commit()


def insert_calories(user_id, fitness):

    calories_data = GD.GetDatasetCalories(StarTime, EndTime, "me", fitness)
    parse_calories_data = PI.parse_calories(calories_data, "Calories")

    daily_data = (
        session.query(DailyData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not daily_data:
        daily_data = DailyData(user_id=user_id, date=yesterday_without_time)
        session.add(daily_data)
        session.flush()
        daily_data_id = daily_data.daily_data_id
    else:
        daily_data_id = daily_data.daily_data_id

    for data_point in parse_calories_data["Calories"]:
        new_calories = Calories(
            daily_data_id=daily_data_id,
            calories=data_point["Calories"],
        )
        session.add(new_calories)
    session.commit()


def insert_Weight(user_id, fitness):

    weight_data = GD.GetDatasetWeight(StarTime, EndTime, "me", fitness)
    parse_weight_data = PI.parse_weight(weight_data, "Weight")

    daily_data = (
        session.query(DailyData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not daily_data:
        daily_data = DailyData(user_id=user_id, date=yesterday_without_time)
        session.add(daily_data)
        session.flush()
        daily_data_id = daily_data.daily_data_id
    else:
        daily_data_id = daily_data.daily_data_id

    for data_point in parse_weight_data["Weight"]:
        new_weight = Weight(
            daily_data_id=daily_data_id,
            weight=data_point["Weight"],
        )
        session.add(new_weight)
    session.commit()


def insert_body_fat(user_id, fitness):

    body_fat_data = GD.GetDatasetBodyFat(StarTime, EndTime, "me", fitness)
    parse_body_fat_data = PI.parse_body_fat(body_fat_data, "Body Fat")

    daily_data = (
        session.query(DailyData)
        .filter_by(user_id=user_id, date=yesterday_without_time)
        .first()
    )

    if not daily_data:
        daily_data = DailyData(user_id=user_id, date=yesterday_without_time)
        session.add(daily_data)
        session.flush()
        daily_data_id = daily_data.daily_data_id
    else:
        daily_data_id = daily_data.daily_data_id

    for data_point in parse_body_fat_data["Body Fat"]:
        new_body_fat = BodyFat(
            daily_data_id=daily_data_id,
            body_fat_pc=data_point["BodyFatPc"],
        )
        session.add(new_body_fat)
    session.commit()


def insert_sleep(user_id, fitness):

    sleep_data = GD.GetDatasetSleep(StarTime, EndTime, "me", fitness)
    parse_sleep_data = PI.parse_sleep(sleep_data, "Sleep")

    paciente = session.query(Paciente).filter_by(user_id=user_id).first()

    user_id = paciente.user_id

    for data_point in parse_sleep_data["Sleep"]:
        new_sleep = Sleep(
            user_id=user_id,
            sleep_type=data_point["Sleep_minutes"],
            time_recorded=data_point["Date"],
        )
        session.add(new_sleep)
    session.commit()
