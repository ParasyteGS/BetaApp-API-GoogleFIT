import Functions.TimeFunctions as tf


def GetDatasetHearRate(StartTime: str, EndTime: str, UserID: str, fitness):

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.heart_rate.bpm"},
        ],
        "bucketByTime": {"durationMillis": 60000},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    HeartData = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return HeartData


def GetDatasetOxSaturation(StartTime: str, EndTime: str, UserID: str, fitness):  # Daily

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.oxygen_saturation"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    OxSaturationData = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return OxSaturationData


def GetDatasetBloodPressure(
    StartTime: str, EndTime: str, UserID: str, fitness
):  # daily

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.blood_pressure"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    BloodPressureData = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return BloodPressureData


def GetDatasetBodyFat(StartTime: str, EndTime: str, UserID: str, fitness):  # Daily

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.body.fat.percentage"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    BodyFatData = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return BodyFatData


def GetDatasetHeight(StartTime: str, EndTime: str, UserID: str, fitness):  # Una vez

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.height"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    Height = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return Height


def GetDatasetWeight(StartTime: str, EndTime: str, UserID: str, fitness):  # Daily

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.weight"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    Weight = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return Weight


# Actividad


def GetDatasetActivity(StartTime: str, EndTime: str, UserID: str, fitness):  # Minutely

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.activity.segment"},
        ],
        "bucketByTime": {"durationMillis": 60000},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    Activity = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return Activity


# Calorias quemadas


def GetDatasetCalories(StartTime: str, EndTime: str, UserID: str, fitness):  # Daily

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.calories.expended"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    Calories = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return Calories


# Minutos de actividad


def GetDatasetActivityMinutes(
    StartTime: str, EndTime: str, UserID: str, fitness
):  # Daily

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.active_minutes"},
        ],
        "bucketByTime": {"period": {"type": "day", "value": 1, "timeZoneId": "GMT"}},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    ActivityMinutes = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return ActivityMinutes


# Sueño


def GetDatasetSleep(StartTime: str, EndTime: str, UserID: str, fitness):  # Hourly

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.sleep.segment"},
        ],
        "bucketByTime": {"durationMillis": 3600000},
        "startTimeMillis": tf.TimeToMillis(StartTime),
        "endTimeMillis": tf.TimeToMillis(EndTime),
    }

    Sleep = (
        fitness.users()
        .dataset()
        .aggregate(
            userId=UserID,
            body=body,
        )
        .execute()
    )

    return Sleep
