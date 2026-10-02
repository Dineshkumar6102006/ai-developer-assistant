from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:password@localhost:3306/ai_dev_assistant"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from app.routes import auth, chat, documents, dashboard

app.register_blueprint(auth.bp)
app.register_blueprint(chat.bp)
app.register_blueprint(documents.bp)
app.register_blueprint(dashboard.bp)

@app.route("/")
def index():
    return "AI Developer Assistant API is running."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
