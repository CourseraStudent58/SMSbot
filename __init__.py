from flask import Flask, render_template, request
from config import Config
from cpaas import Cpaas
from menubot import MenuBot
from menuform import MenuForm
from setupform import SetupForm
from logger import log

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

bot = MenuBot()
cpaas = Cpaas(bot)


@app.route('/inbound-sms/webhook', methods=['POST'])
def webhook():
    log("webhook");
    bot.loadMenu()
    return cpaas.post()


@app.route('/', methods=['GET'])
def home():
    log("home")
    return render_template('index.html',
                           title="SMSbot Demo",
                           description="A generic SMS bot application for the AT&T API Marketplace",
                           setupStatus=cpaas.getStatus(),
                           menuStatus=bot.getStatus())


@app.route('/menu', methods=('GET', 'POST'))
def menu():
    log("menu")

    form = MenuForm(request.form)
    response = form.http()
    return response


@app.route('/setup', methods=('GET', 'POST'))
def config():
    log("/setup")
    form = SetupForm(request.form)
    response = form.http_request()
    return response


@app.route('/success', methods=('GET', 'POST'))
def success():
    log("/success")
    return render_template('success.html',
                           template='success-template')


if __name__ == '__main__':
    app.run()  # host='0.0.0.0', ssl_context=('server.crt','server.key'))
