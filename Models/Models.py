class HeartRate:
    def __init__(self, time_sample=None, AvValue=0.0, MinValue=0.0, MaxValue=0.0):
        self.time = time_sample
        self.value = AvValue
        self.min = MinValue
        self.max = MaxValue

    def to_dict(self):
        return {
            "Av_ppm": self.value,
            "Min_ppm": self.min,
            "Max_ppm": self.max,
            "Date": self.time,
        }


class OxygenSaturation:
    def __init__(self, time_sample=None, Avvalue=0.0, MinValue=0.0, MaxValue=0.0):
        self.time = time_sample
        self.value = Avvalue
        self.min = MinValue
        self.max = MaxValue

    def to_dict(self):
        return {
            "AvPc": self.value,
            "MinPc": self.min,
            "MaxPc": self.max,
            "Date": self.time,
        }


class BloddPressure:
    def __init__(
        self,
        time_sample=None,
        SisAv=0.0,
        SisMin=0.0,
        SisMax=0.0,
        DiaAv=0.0,
        DiaMin=0.0,
        DiaMax=0.0,
    ):
        self.time = time_sample
        self.SisAv = SisAv
        self.SisMin = SisMin
        self.SisMax = SisMax
        self.DiaAv = DiaAv
        self.DiaMin = DiaMin
        self.DiaMax = DiaMax

    def to_dict(self):
        return {
            "SisAv": self.Sistolica,
            "SisMin": self.SisMin,
            "SisMax": self.SisMax,
            "DiaAv": self.Diastolica,
            "DiaMin": self.DiaMin,
            "DiaMax": self.DiaMax,
            "Date": self.time,
        }


class BodyFat:
    def __init__(self, time_sample=None, Percentage=0.0):
        self.time = time_sample
        self.value = Percentage

    def to_dict(self):
        return {
            "BodyFatPc": self.value,
            "Date": self.time,
        }


class Height:
    def __init__(self, time_sample=None, value=0.0):
        self.time = time_sample
        self.value = value

    def to_dict(self):
        return {
            "Height": self.value,
            "Date": self.time,
        }


class Weight:
    def __init__(self, time_sample=None, value=0.0):
        self.time = time_sample
        self.value = value

    def to_dict(self):
        return {
            "Weight": self.value,
            "Date": self.time,
        }


class Activity:
    def __init__(self, time_sample=None, value=0.0):
        self.time = time_sample
        self.value = value

    def to_dict(self):
        return {
            "Type Activity": self.value,
            "Date": self.time,
        }


class Calories:
    def __init__(self, time_sample=None, value=0.0):
        self.time = time_sample
        self.value = value

    def to_dict(self):
        return {
            "Calories": self.value,
            "Date": self.time,
        }


class Activity_minutes:
    def __init__(self, time_sample=None, value=0.0):
        self.time = time_sample
        self.value = value

    def to_dict(self):
        return {
            "Activity_minutes": self.value,
            "Date": self.time,
        }


class Sleep:
    def __init__(self, time_sample=None, value=0.0):
        self.time = time_sample
        self.value = value

    def to_dict(self):
        return {
            "Sleep_minutes": self.value,
            "Date": self.time,
        }
