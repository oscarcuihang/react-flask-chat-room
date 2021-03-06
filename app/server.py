import uuid
import pymysql
import pymysql.cursors
from datetime import datetime
from flask import (
  Flask,
  request,
  render_template,
  abort,
  jsonify
)

app = Flask(__name__, static_folder='../static/dist', template_folder='../static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

users = []
messages = dict()
chat = []

def db_excute(sql):
  connection = pymysql.connect(host='127.0.0.1', port=8889, user='root', passwd='root', db='rf_chat_room', cursorclass=pymysql.cursors.DictCursor)
  cursor = connection.cursor()
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello():
  sql = ("INSERT INTO `rf_chat_room`.`users` (`name`, `email`) VALUES ('test name', 'test@name.com')")
  db_excute(sql)
  return '1 World!'

@app.route('/login', methods=['POST'])
def login():
  username = request.json.get('username', None)
  user_name_exists = username in users
  if username is None or user_name_exists:
    abort(401)
  else:
    users.append(username)
    return jsonify({
      'status': '200',
      'msg': 'Login Success'
    })

@app.route('/send', methods=['POST'])
def send():
  username = request.json.get('username', None)
  message = request.json.get('message', None)
  timestamp = datetime.now()
  id = str(uuid.uuid4())

  if username is None or username not in users:
    abort(401)
  if message is None or message == '':
    abort(400)

  messages[id] = {
    'username': username,
    'message': message,
    'timestamp': timestamp,
    'id': id
  }
  chat.append(id)
  return jsonify(messages)

@app.route('/get/<last_id>', methods=['GET'])
def get(last_id):
  if chat is None or len(chat) == 0:
    return jsonify([])

  index = 0
  if last_id:
    try:
      index = chat.index(last_id) + 1
    except ValueError as e:
      abort(400)
  ids_to_return = chat[index:]
  resluts = map(lambda x: messages[x], ids_to_return)
  return jsonify(list(resluts))

@app.route('/update/<last_id>', methods=['GET'])
def update(last_id):
  index = 0
  if last_id:
    try:
      index = chat.index(last_id) + 1
    except ValueError as e:
      abort(400)
  resluts = { 'new_messages': False }
  if index < len(chat):
    resluts['new_messages'] = True
  return jsonify(resluts)


if __name__ == '__main__':
  app.run(debug=True)


