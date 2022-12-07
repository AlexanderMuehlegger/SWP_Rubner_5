from flask import Flask, request
import json

app = Flask(__name__)

with open('saved_statistic.json') as json_file:
    stat_data = json.loads(json_file)

print(stat_data)

@app.route('/api/saveStatistic', methods=['POST'])
def saveStatistic():
    statistic = request.data
    data = json.loads(statistic)
    print(data)    

    return {'Response': 'OK'}

@app.route('/api/getStatistics', methods=["GET"])
def getStatistics():
    return "kdkdk"

app.run()