import flask
from flask_cors import CORS, cross_origin
from src.utlis import write_logs,get_error_message,get_success_message

app = flask.Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def ping():
    try:
        return flask.Response(response=get_success_message("Success"), status=200, content_type='application/json')
    except Exception as e:
        write_logs("ERROR",str(e))
        return flask.Response(response=get_error_message("Internal Server Error."), status=200, content_type='application/json')

@app.route('/logs', methods=['POST'])
@cross_origin()
def logs():
    try:
        write_logs("INFO",flask.request.data.decode('utf-8'))
        return flask.Response(response=get_success_message("Success"), status=200, content_type='application/json')
    except Exception as e:
        write_logs("ERROR",str(e))
        return flask.Response(response=get_error_message("Internal Server Error."), status=200, content_type='application/json')
    
# main driver function
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9090)