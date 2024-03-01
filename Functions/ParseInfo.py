from datetime import datetime
from typing import List
import Models.Models as MD
import Functions.TimeFunctions as tf
from types import SimpleNamespace
from Models.const import MapaActividades, MapSleepType


def parse_heart_bpm(ds, data_type: str) -> List[MD.HeartRate]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.HeartRate()
                row.value = p["value"][0]["fpVal"]
                row.max = p["value"][1]["fpVal"]
                row.min = p["value"][2]["fpVal"]
                row.time = tf.NanoToTime(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_ox_saturation(ds, data_type: str) -> List[MD.OxygenSaturation]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.OxygenSaturation()
                row.value = round(p["value"][0]["fpVal"], 2)
                row.max = p["value"][1]["fpVal"]
                row.min = p["value"][2]["fpVal"]
                row.time = tf.NanoToTimeWoHours(p["startTimeNanos"])
                row.type = data_type
                data.append(row.to_dict())

    return {data_type: data}


def parse_blood_pressure(ds, data_type: str) -> List[MD.BloddPressure]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.BloddPressure()
                row.SisAv = p["value"][0]["fpVal"]
                row.SisMax = p["value"][1]["fpVal"]
                row.SisMin = p["value"][2]["fpVal"]
                row.DiaAv = p["value"][3]["fpVal"]
                row.DiaMax = p["value"][4]["fpVal"]
                row.DiaMin = p["value"][5]["fpVal"]
                row.time = tf.NanoToTime(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_body_fat(ds, data_type: str) -> List[MD.BodyFat]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.BodyFat()
                row.value = round(p["value"][0]["fpVal"], 2)
                row.time = tf.NanoToTimeWoHours(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_height(ds, data_type: str) -> List[MD.Height]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.Height()
                row.value = p["value"][1]["fpVal"]
                row.time = tf.NanoToTime(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_weight(ds, data_type: str) -> List[MD.Weight]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.Weight()
                row.value = p["value"][1]["fpVal"]
                row.time = tf.NanoToTimeWoHours(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_activity(ds, data_type: str) -> List[MD.Activity]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.Activity()
                row.value = MapaActividades[p["value"][0]["intVal"]]
                row.time = tf.NanoToTime(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_calories(ds, data_type: str) -> List[MD.Calories]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.Calories()
                row.value = p["value"][0]["fpVal"]
                row.time = tf.NanoToTimeWoHours(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_sleep(ds, data_type: str) -> List[MD.Sleep]:

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.Sleep()
                row.value = MapSleepType[p["value"][0]["intVal"]]
                row.time = tf.NanoToTime(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data


def parse_activity_minutes(ds, data_type: str) -> List[MD.Activity_minutes]:  # Daily

    data = []

    for res in ds["bucket"]:
        for ds_item in res["dataset"]:
            for p in ds_item["point"]:
                row = MD.Activity_minutes()
                row.value = p["value"][0]["intVal"]
                row.time = tf.NanoToTimeWoHours(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data
