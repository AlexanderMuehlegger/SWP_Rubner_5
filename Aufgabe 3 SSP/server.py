from flask import Flask, request
import json
import sqlite3

app = Flask(__name__)
db_string = "Statistic.db"

@app.route('/api/saveStatistic', methods=['POST'])
def saveStatistic():
    
    try:
        data = request.get_json(force=True)
        print(data)
        with sqlite3.connect(db_string) as conn:
            cur = conn.cursor()
            
            cur.execute("INSERT INTO Statistic (id, username, symbol_anz, result) VALUES (NULL, ?, ?, ?);", [data['username'], str(data['statistics']), str(data['result'])])
            
            return {'Response': 'Data inserted!'}
    except Exception as e:
        print(e)
        return {'Error': 'Something went wrong turing insert!'}
        

@app.route('/api/getPlayerStat/<username>', methods=['GET'])
def getPlayerStat(username):
    if username == "":
        return {'ERROR': 'No username Entered'}
    with sqlite3.connect(db_string) as conn:
        cur = conn.cursor()
        result = cur.execute("SELECT json_object('id', id, 'username',username, 'symbol_anz', symbol_anz, 'result', result) FROM Statistic WHERE username=?", [username])
        result = result.fetchall()
        if(result != []):
            return json.dumps(result)
    return {'ERROR': 'Something went wrong!'}

@app.route('/api/getStatistics  ', methods=["GET"])
def getStatistics():
    with sqlite3.connect(db_string) as conn:
        cur = conn.cursor()
        result = cur.execute("SELECT * FROM Statistic")
        data = result.fetchall()

        return json.dumps(data)



if __name__ == "__main__":
    app.run()