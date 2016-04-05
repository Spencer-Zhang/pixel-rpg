from flask import Flask
from managers.user import UserManager

from users import bp_users

app = Flask(__name__)

app.register_blueprint(bp_users)

if __name__ == '__main__':
  app.run(debug=True)
