import auth
import task
import celeryconfig
from  celery_init import celery_init_app
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.register_blueprint(auth.auth_blueprint)
app.register_blueprint(task.task_blueprint)
app.config["MAIL_SERVER"] = "smtp.example.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "your-email@example.com" 
app.config["MAIL_PASSWORD"] = "yourpassword" 
app.config["MAIL_USE_TLS"] = True


celery = celery_init_app(app)
celery.config_from_object(celeryconfig)
mail = Mail(app)