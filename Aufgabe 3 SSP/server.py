from flask import Flask, request

app = Flask(__name__)

@app.route('/api/saveStatistic', methods=['POST'])
def saveStatistic():
    statistic = request.data
    print(statistic)

@app.route('/api/getStatistics', methods=["GET"])
def getStatistics():
    return "kdkdk"

app.run()