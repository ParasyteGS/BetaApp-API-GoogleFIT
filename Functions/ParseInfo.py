from datetime import datetime
from typing import List
import Models.Models as MD
import Functions.TimeFunctions as tf
from types import SimpleNamespace


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
                row.value = p["value"][0]["fpVal"]
                row.max = p["value"][1]["fpVal"]
                row.min = p["value"][2]["fpVal"]
                row.time = tf.NanoToTime(p["startTimeNanos"])
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
                row.value = p["value"][0]["fpVal"]
                row.time = tf.NanoToTime(p["startTimeNanos"])
                data.append(row.to_dict())
    final_data = {data_type: data}

    return final_data
