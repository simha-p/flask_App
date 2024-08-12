from flask import Flask, jsonify, request
from data_storage import data_storage

app= Flask(__name__)

mock_data={
    "data":[1,2,3,4,5,6]
}

@app.route('/', methods=['GET'])
def hello():
    return jsonify("Flask Application")
#for data retrival
@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    return jsonify(mock_data)


#Data Processing 

def process_data(data):
    return sum(data)

#processed data retrival

@app.route('/get_processed_data', methods=['GET'])
def get_processed_data():
    data=mock_data['data']
    processed_data=process_data(data)

    data_storage['processed_data']=processed_data
    return jsonify({"processed_data": processed_data})
if __name__=='__main__':
    app.run(debug=True)