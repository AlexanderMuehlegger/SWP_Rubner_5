from flask import Flask, request
import json
import sqlite3

app = Flask(__name__)
db_string = "Statistic.db"

@app.route('/api/saveStatistic', methods=['POST'])
def saveStatistic():
    
    try:
        data = request.get_json(force=True)
        #TODO: finish insert into db
        #TODO: add response
        print(data)
        with sqlite3.connect(db_string) as conn:
            cur = conn.cursor()
            
            cur.execute("INSERT INTO Statistic (id, username, symbol_anz, result) VALUES (NULL, ?, ?, ?);", [data['username'], str(data['statistics']), str(data['result'])])
            
            return {'Response': 'Data inserted!'}
    except Exception as e:
        print(e)
        return {'Error': 'Something went wrong turing insert!'}
        

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