from flask import Flask, request
import json
import sqlite3

app = Flask(__name__)
db_string = "Statistic.db"

@app.route('/api/saveStatistic', methods=['POST'])
def saveStatistic():
    data = request.get_data().decode("UTF-8")
    #TODO: finish insert into db
    #TODO: add response
    with sqlite3.connect(db_string) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Statistic WHERE username=?", [data['username']])
        if cur.fetchall() is 0:
            cur.execute("INSERT INTO Statistic (id, username, symbol_anz) VALUES (NULL, ?, ?);", [])
    return {'Response': 'OK'}

@app.route('/api/getStatistics', methods=["GET"])
def getStatistics():
    with sqlite3.connect(db_string) as conn:
        cur = conn.cursor()
        result = cur.execute("SELECT * FROM Statistic")
        data = result.fetchall()

        return json.dumps(data)

#TODO: add website for data output


if __name__ == "__main__":
    app.run()