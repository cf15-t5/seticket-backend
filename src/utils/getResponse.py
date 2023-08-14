from flask import jsonify
def success(data,message):
  response = jsonify( {
    'status_code': 200,
    'message': message,
    'data': data
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response
   
def error(errors,message):
    response = jsonify({
      'status_code': 400,
      'message': message,
      'data': errors
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response