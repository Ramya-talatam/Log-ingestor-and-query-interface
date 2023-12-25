from flask import Flask, render_template,request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
#from bson import json_util

app = Flask(__name__)

uri = "mongodb+srv://logentry:logingest@cluster0.yrxldvn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['logdata'] 
logs_collection = db['logs'] 


@app.route('/', methods=['GET','POST'])
def index():
    log = logs_collection.find()
    return render_template('ui.html', logs=log)

@app.route('/filter_logs', methods=['GET'])
def filter_logs():
    level = request.args.get('level', '')
    message = request.args.get('message', '')
    resource_id = request.args.get('resourceId', '')
    timestamp = request.args.get('timestamp', '')
    trace_id = request.args.get('traceId', '')
    span_id = request.args.get('spanId', '')
    commit = request.args.get('commit', '')
    parent_resource_id = request.args.get('parentResourceId', '')

    filter_query = {}
    fq=[]
    if level:
        filter_query['level'] = level
        fq.append(level)
    if message:
        regex_pattern = f'.*{message}.*'
        filter_query['message'] ={'$regex' :regex_pattern,'$options':"i"}
        fq.append(message)
    if resource_id:
        filter_query['resourceId'] = resource_id
        fq.append(resource_id)
    if timestamp:
        filter_query['timestamp'] = timestamp
        fq.append(timestamp)
    if trace_id:
        filter_query['traceId'] = trace_id
        fq.append(trace_id)
    if span_id:
        filter_query['spanId'] = span_id
        fq.append(span_id)
    if commit:
        filter_query['commit'] = commit
        fq.append(commit)
    if parent_resource_id:
        filter_query['metadata'] = {'parentResourceId':parent_resource_id}
        fq.append(parent_resource_id)
   
    filtered_logs = list(logs_collection.find(filter_query))
    return render_template('ui.html', logs=filtered_logs, filter_query=fq)


if __name__ == '__main__':
    app.run(port=5000, threaded=True)
