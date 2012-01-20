import flask

app = flask.Flask(__name__)

def validate_user(user):
    '''To complete for user auth'''
    return True

@app.route('/<user>/<type>/<key>', methods=['get', 'post', 'put', 'delete'])
def full(user, type, key):
    '''Anyone get anything and search but only a 
       autherized user can post a new item or delete one'''
    
    resp = flask.Response('')
    req = flask.request
    query_string = flask.request.query_string
    path = flask.request.path

    # only allow valid user to do non get request or not search
    if req.method != 'GET' and key != '_search':
        if not validate_user(user):
            raise 

    resp.headers['X-Accel-Redirect'] = "/elastic/%s?%s" % (path, query_string)
    return resp

@app.route('/<user>/<type>', methods=['get', 'post', 'delete'])
def type(user, type):
    '''Anyone get and search across an index but only a 
       authorized user can create or delete an elastic search type'''
    
    req = flask.request
    query_string = flask.request.query_string
    path = flask.request.path

    if type != '_search' and req.method != 'GET' and type[0] == '_':
        return 'Authentication Error', 403

    if type[0] != '_' and req.method != 'GET':
        validate_user(user)

    resp = flask.Response('')
    resp.headers['X-Accel-Redirect'] = "/elastic/%s?%s" % (path, query_string)
    return resp

@app.route('/<user>', methods=['get'])
def user(user):
    '''user could infact be a _search and we 
    allow anyone to search across all data'''

    resp = flask.Response('')
    req = flask.request
    query_string = flask.request.query_string
    path = flask.request.path

    resp.headers['X-Accel-Redirect'] = "/elastic/%s?%s" % (path, query_string)
    return resp

@app.route('/', methods=['get'])
def base():
    '''just to see the elatic search root'''
    resp = flask.Response('')
    req = flask.request
    query_string = flask.request.query_string
    path = flask.request.query_string
    resp.headers['X-Accel-Redirect'] = "/elastic/%s?%s" % (path, query_string)
    return resp


if __name__ == "__main__":
    app.run(debug=True)
