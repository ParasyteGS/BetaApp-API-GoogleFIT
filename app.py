import os
import flask
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import datetime as dt
import json
import time
from types import SimpleNamespace


# Funciones necesarias para obtener los datos de la API de Google Fit
import Functions.GetData as GD
import Functions.ParseInfo as PI

# Conexión a la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.CreateDB import *

# Guardar Base de datos
import Functions.scheduled_tasks as ST

CLIENT_SECRET_FILE = "client_secret.json"
SCOPES = [
    "openid email profile https://www.googleapis.com/auth/fitness.activity.read https://www.googleapis.com/auth/fitness.blood_glucose.read https://www.googleapis.com/auth/fitness.blood_pressure.read https://www.googleapis.com/auth/fitness.body.read https://www.googleapis.com/auth/fitness.body_temperature.read https://www.googleapis.com/auth/fitness.heart_rate.read https://www.googleapis.com/auth/fitness.location.read https://www.googleapis.com/auth/fitness.nutrition.read https://www.googleapis.com/auth/fitness.oxygen_saturation.read https://www.googleapis.com/auth/fitness.reproductive_health.read https://www.googleapis.com/auth/fitness.sleep.read https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
]
API_SERVICE_NAME = "fitness"
API_VERSION = "v1"

app = flask.Flask(__name__)
app.secret_key = "random secret"

engine = create_engine("postgresql://postgres:alex2134@localhost:5432/neurohdb")
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def index():
    if "credentials" in flask.session:
        return flask.redirect(flask.url_for("test_api_request"))
    else:
        return flask.render_template("index.html")


def height_data(fitness):
    # Obtener la altura del usuario
    StartTime = dt.datetime(2024, 1, 1, 0, 0, 0)
    EndTime = dt.datetime.now()
    height_data = GD.GetDatasetHeight(StartTime, EndTime, "me", fitness)
    parse_height_data = PI.parse_height(height_data, "Height")
    return parse_height_data


@app.route("/Gracias")
def test_api_request():
    if "credentials" not in flask.session:
        return flask.redirect("authorize")
    credentials = google.oauth2.credentials.Credentials(**flask.session["credentials"])
    fitness = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )

    userinfo_service = googleapiclient.discovery.build(
        "oauth2", "v2", credentials=credentials
    )
    user_info = userinfo_service.userinfo().get().execute()

    paciente = session.query(Paciente).filter_by(email=user_info["email"]).first()

    user_id = paciente.user_id

    # # MinuteData
    # ST.inser_heart_rate(user_id, fitness)
    # ST.insert_oxygen(user_id, fitness)
    # ST.insert_blood_pressure(user_id, fitness)
    # ST.inser_activity_type(user_id, fitness)

    # # DailyData

    # ST.insert_body_fat(user_id, fitness)
    # ST.insert_calories(user_id, fitness)

    # ST.insert_Weight(user_id, fitness)
    # ST.insert_activity_minutes(user_id, fitness)

    # ST.insert_sleep(user_id, fitness)

    flask.session["credentials"] = credentials_to_dict(credentials)
    return flask.render_template("Gracias.html", user_info=user_info)


@app.route("/authorize")
def authorize():
    if "credentials" in flask.session:
        return flask.render_template("Gracias.html")

    else:
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            CLIENT_SECRET_FILE, scopes=SCOPES
        )

        flow.redirect_uri = flask.url_for("oauth2callback", _external=True)

        authorization_url, state = flow.authorization_url(
            access_type="offline",
            include_granted_scopes="true",
        )

        flask.session["state"] = state

        return flask.redirect(authorization_url)


@app.route("/oauth2callback")
def oauth2callback():

    state = flask.session["state"]

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES, state=state
    )
    flow.redirect_uri = flask.url_for("oauth2callback", _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    # Obtener información del usuario:
    fitness = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )
    userinfo_service = googleapiclient.discovery.build(
        "oauth2", "v2", credentials=credentials
    )
    user_info = userinfo_service.userinfo().get().execute()

    parse_height_data = height_data(fitness)

    Height = parse_height_data["Height"][0]["Height"]

    paciente = session.query(Paciente).filter_by(email=user_info["email"]).first()
    if not paciente:
        new_paciente = Paciente(
            first_name=user_info.get("given_name", ""),
            last_name=user_info.get("family_name", ""),
            email=user_info["email"],
            access_token=credentials.token,
            refresh_token=credentials.refresh_token,
            height=Height,
        )
        session.add(new_paciente)
    else:
        paciente.access_token = credentials.token
        paciente.refresh_token = credentials.refresh_token
    session.commit()

    flask.session["credentials"] = credentials_to_dict(credentials)

    return flask.redirect(flask.url_for("test_api_request"))


def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }


if __name__ == "__main__":
    os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    app.run("localhost", port=8080, debug=True)
