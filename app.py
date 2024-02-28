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

CLIENT_SECRET_FILE = "client_secret.json"
SCOPES = [
    "https://www.googleapis.com/auth/fitness.activity.read https://www.googleapis.com/auth/fitness.blood_glucose.read https://www.googleapis.com/auth/fitness.blood_pressure.read https://www.googleapis.com/auth/fitness.body.read https://www.googleapis.com/auth/fitness.body_temperature.read https://www.googleapis.com/auth/fitness.heart_rate.read https://www.googleapis.com/auth/fitness.location.read https://www.googleapis.com/auth/fitness.nutrition.read https://www.googleapis.com/auth/fitness.oxygen_saturation.read https://www.googleapis.com/auth/fitness.reproductive_health.read https://www.googleapis.com/auth/fitness.sleep.read"
]
API_SERVICE_NAME = "fitness"
API_VERSION = "v1"

app = flask.Flask(__name__)
app.secret_key = "random secret"


@app.route("/")
def index():
    return print_index_table()


# Dame el modelamiento de la base de datos de donde se guarden los siguientes valores: usuario, heart_bpm, oxigen_saturation, wheight, blood_pressure


@app.route("/test")
def test_api_request():
    if "credentials" not in flask.session:
        return flask.redirect("authorize")
    credentials = google.oauth2.credentials.Credentials(**flask.session["credentials"])

    fitness = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )
    lista = fitness.users().dataSources().list(userId="me").execute()

    Time = dt.datetime.now()
    StartTime = dt.datetime(Time.year, Time.month, Time.day, 0, 0, 0)
    EndTime = dt.datetime(Time.year, Time.month, Time.day, 23, 59, 0)

    HeartData = GD.GetDatasetHearRate(StartTime, EndTime, "me", fitness)

    HData = PI.parse_heart_bpm(HeartData, "Heart Rate")
    OxygenData = GD.GetDatasetOxSaturation(StartTime, EndTime, "me", fitness)
    OData = PI.parse_ox_saturation(OxygenData, "Oxygen Saturation")

    BloodPressureData = GD.GetDatasetBloodPressure(StartTime, EndTime, "me", fitness)
    BPData = PI.parse_blood_pressure(BloodPressureData, "Blood Pressure")

    flask.session["credentials"] = credentials_to_dict(credentials)
    return OData


@app.route("/authorize")
def authorize():
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
    flask.session["credentials"] = credentials_to_dict(credentials)

    return flask.redirect(flask.url_for("test_api_request"))


@app.route("/revoke")
def revoke():
    if "credentials" not in flask.session:
        return (
            'You need to <a href="/authorize">authorize</a> before '
            "testing the code to revoke credentials."
        )

    credentials = google.oauth2.credentials.Credentials(**flask.session["credentials"])

    revoke = requests.post(
        "https://oauth2.googleapis.com/revoke",
        params={"token": credentials.token},
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    status_code = getattr(revoke, "status_code")
    if status_code == 200:
        return "Credentials successfully revoked" + print_index_table()
    else:
        return "An error occurred." + print_index_table()


@app.route("/clear")
def clear_credentials():
    if "credentials" in flask.session:
        del flask.session["credentials"]
    return "Credentials have been cleared.<br><br>" + print_index_table()


def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }


def print_index_table():
    return (
        "<table>"
        + '<tr><td><a href="/test">Test an API request</a></td>'
        + "<td>Submit an API request and see a formatted JSON response. "
        + "    Go through the authorization flow if there are no stored "
        + "    credentials for the user.</td></tr>"
        + '<tr><td><a href="/authorize">Test the auth flow directly</a></td>'
        + "<td>Go directly to the authorization flow. If there are stored "
        + "    credentials, you still might not be prompted to reauthorize "
        + "    the application.</td></tr>"
        + '<tr><td><a href="/revoke">Revoke current credentials</a></td>'
        + "<td>Revoke the access token associated with the current user "
        + "    session. After revoking credentials, if you go to the test "
        + "    page, you should see an <code>invalid_grant</code> error."
        + "</td></tr>"
        + '<tr><td><a href="/clear">Clear Flask session credentials</a></td>'
        + "<td>Clear the access token currently stored in the user session. "
        + '    After clearing the token, if you <a href="/test">test the '
        + "    API request</a> again, you should go back to the auth flow."
        + "</td></tr></table>"
    )


if __name__ == "__main__":
    os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    app.run("localhost", port=8080, debug=True)
