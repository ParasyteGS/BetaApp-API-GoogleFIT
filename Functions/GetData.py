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


def GetDatasetOxSaturation(StartTime: str, EndTime: str, UserID: str, fitness):

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.oxygen_saturation"},
        ],
        "bucketByTime": {"durationMillis": 60000},
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


def GetDatasetBloodPressure(StartTime: str, EndTime: str, UserID: str, fitness):

    body = {
        "aggregateBy": [
            {"dataTypeName": "com.google.blood_pressure"},
        ],
        "bucketByTime": {"durationMillis": 60000},
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


def GetDatasetHeight(StartTime: str, EndTime: str, UserID: str, fitness):

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


def GetDatasetWeight(StartTime: str, EndTime: str, UserID: str, fitness):

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
