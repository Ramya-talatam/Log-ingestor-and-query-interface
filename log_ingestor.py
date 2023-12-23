from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://logentry:logingest@cluster0.yrxldvn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['logdata'] 
logs_collection = db['logs'] 
app = Flask(__name__)



# below is the curl script to populate single log entry at a time into log ingestor(for testing purpose)

# Invoke-WebRequest -Uri 'http://localhost:3000/ingest' -Method Post -Headers @{
#     'Content-Type' = 'application/json'
# } -Body '{
#     "level": "error",
#     "message": "Failed to connect to DB",
#     "resourceId": "server-1234",
#     "timestamp": "2023-09-15T08:00:00Z",
#     "traceId": "abc-xyz-123",
#     "spanId": "span-456",
#     "commit": "5e5342f",
#     "metadata": {
#         "parentResourceId": "server-0987"
#     }
# }'


#below is the curl script to populate multiple log entries at once into log ingestor(for testing purpose)

# $logs = Get-Content -Raw -Path .\logs.json | ConvertFrom-Json
# $url = "http://localhost:3000/ingest"
# $headers = @{
#     "Content-Type" = "application/json"
# }

# foreach ($log in $logs) {
#     $logJson = $log | ConvertTo-Json
#     Invoke-WebRequest -Uri $url -Method Post -Headers $headers -Body $logJson
# }


@app.route('/', methods=['POST'])
def ingest_log():
    try:
        data = request.get_json()
        required_fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'metadata']
        for field in required_fields:
            if field not in data:
                return jsonify({'status': 'error', 'message': f'Missing required field: {field}'})

        result = logs_collection.insert_one(data)

        return jsonify({'status': 'success', 'message': 'Log ingested successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
if __name__ == '__main__':
    app.run(port=3000, threaded=True)
