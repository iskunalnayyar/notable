import datetime
import os
import sqlite3

from flask import Flask, render_template, Response

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "interview-app.db")


@app.route('/doctors')
def list_of_doctors():
    conn = sqlite3.connect(db_path)
    doctors_list = conn.execute('SELECT * FROM doctors').fetchall()

    doctors_list_formatted = []
    for doc in doctors_list:
        doctors_list_formatted.append([
            doc[1],
            doc[2]
        ])
    return render_template('doctors.html', doctors=doctors_list_formatted)


@app.route("/doctor/<int:id>/<string:selected_date>")
def select_doctor(id, selected_date):
    conn = sqlite3.connect(db_path)
    date_time_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    doctor_list = conn.execute(
        'SELECT * FROM appointments WHERE doctor_id = ? AND date(created_datetime) = ?', [id, date_time_obj]).fetchall()

    doctors_list_formatted = []
    for doc in doctor_list:
        doctors_list_formatted.append([
            doc[1],
            doc[2]
        ])

    return render_template('doctors_appointments.html', doctors=doctors_list_formatted)


@app.route("/doctor/<int:id>/delete/<int:appointment_id>")
def delete_appointment(id, appointment_id):
    conn = sqlite3.connect(db_path)
    delete_app = conn.execute(
        'DELETE FROM appointments WHERE doctor_id = ? AND appointment_id = ?', [id, appointment_id]).fetchall()
    if delete_app:
        return Response("Success", status=200)
    else:
        return Response("Failed", status=404)


@app.route("/doctor/<int:id>/add/<string:selected_date>")
def add_appointment(id, selected_date):
    date_time_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%dT%H:%M:%S")
    date_time_obj_min = date_time_obj.minute

    conn = sqlite3.connect(db_path)
    if date_time_obj_min % 15 == 0:
        conn.execute("INSERT INTO appointments(appointment_id, created_datetime, patient_id, doctor_id, visit_type) "
                     "VALUES(6, ?, 1, ?, 1)", [date_time_obj, id]),
        return Response("Success", status=200)
    else:
        return Response("Failed", status=404)


if __name__ == '__main__':
    app.run(debug=True)
