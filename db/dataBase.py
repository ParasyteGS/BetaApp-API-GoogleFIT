# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:18:53 2024

@author: JBocanegra
"""

# CREACIÓN DE LA BASE DE DATOS

import sqlite3

# Conexión a la base de datos (crea la base de datos si no existe)
conn = sqlite3.connect('medical_data.db')
cur = conn.cursor()

# Creación de la tabla request_history
cur.execute('''CREATE TABLE IF NOT EXISTS request_history (
                    request_datetime TEXT,
                    user_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES pacientes(user_id)
                )''')

# Creación de la tabla pacientes
cur.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                    user_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    weight INTEGER,
                    height REAL,
                    email TEXT,
                    gender TEXT,
                    phone_n INTEGER,
                    stress INTEGER,
                    bodyFat_p INTEGER,
                    hours_sleep REAL,
                    activity INTEGER,
                    activity_m REAL,
                    calories REAL
                )''')

# Creación de la tabla heart_rate
cur.execute('''CREATE TABLE IF NOT EXISTS heart_rate (
                    user_id INTEGER,
                    r_datetime TEXT,
                    avValue REAL,
                    maxValue REAL,
                    minValue REAL,
                    sample_t TEXT,
                    FOREIGN KEY (user_id) REFERENCES pacientes(user_id)
                )''')

# Creación de la tabla sp02
cur.execute('''CREATE TABLE IF NOT EXISTS sp02 (
                    user_id INTEGER,
                    r_datetime TEXT,
                    avValue REAL,
                    maxValue REAL,
                    minValue REAL,
                    sample_t TEXT,
                    FOREIGN KEY (user_id) REFERENCES pacientes(user_id)
                )''')

# Creación de la tabla pressure
cur.execute('''CREATE TABLE IF NOT EXISTS pressure (
                    user_id INTEGER,
                    r_datetime TEXT,
                    sisAv REAL,
                    sisMax REAL,
                    sisMin REAL,
                    diaAv REAL,
                    diaMax REAL,
                    diaMin REAL,
                    sample_t TEXT,
                    FOREIGN KEY (user_id) REFERENCES pacientes(user_id)
                )''')

# Commit y cierre de la conexión
conn.commit()
conn.close()

#%% Ejemplo de cómo insertar datos a la base de datos

import sqlite3
from datetime import datetime

# Función para insertar datos de pacientes
def insert_paciente(conn, cursor, paciente_data):
    cursor.execute('''INSERT INTO pacientes (
                        user_id, first_name, last_name, weight, height, email,
                        gender, phone_n, stress, bodyFat_p, hours_sleep,
                        activity, activity_m, calories
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    paciente_data)
    conn.commit()

# Función para insertar datos de ritmo cardíaco
def insert_heart_rate(conn, cursor, heart_rate_data):
    cursor.execute('''INSERT INTO heart_rate (
                        user_id, r_datetime, avValue, maxValue, minValue, sample_t
                    ) VALUES (?, ?, ?, ?, ?, ?)''',
                    heart_rate_data)
    conn.commit()

# Función para insertar datos de spO2
def insert_sp02(conn, cursor, sp02_data):
    cursor.execute('''INSERT INTO sp02 (
                        user_id, r_datetime, avValue, maxValue, minValue, sample_t
                    ) VALUES (?, ?, ?, ?, ?, ?)''',
                    sp02_data)
    conn.commit()

# Función para insertar datos de presión arterial
def insert_pressure(conn, cursor, pressure_data):
    cursor.execute('''INSERT INTO pressure (
                        user_id, r_datetime, sisAv, sisMax, sisMin, diaAv, diaMax, diaMin, sample_t
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    pressure_data)
    conn.commit()

# Conexión a la base de datos
conn = sqlite3.connect('medical_data.db')
cursor = conn.cursor()

#%% Aquí se cambian por los datos que genera la API

# Ejemplo de datos para insertar (reemplaza con los datos reales obtenidos de la API)
paciente_data = (1, 'Juan', 'Pérez', 70, 1.75, 'juan@example.com', 'masculino', 123456789, 5, 20, 8, 1, 1000, 2000)
heart_rate_data = (1, datetime.now().isoformat(), 80, 100, 60, '1 min')
sp02_data = (1, datetime.now().isoformat(), 98, 99, 97, '1 min')
pressure_data = (1, datetime.now().isoformat(), 120, 130, 110, 80, 90, 70, '1 min')

#%% 

# Insertar datos en las tablas correspondientes
insert_paciente(conn, cursor, paciente_data)
insert_heart_rate(conn, cursor, heart_rate_data)
insert_sp02(conn, cursor, sp02_data)
insert_pressure(conn, cursor, pressure_data)

# Cerrar la conexión
conn.close()


