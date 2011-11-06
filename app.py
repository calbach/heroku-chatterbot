import os
from flask import Flask
from flask import request
from chatterbotapi import ChatterBotFactory, ChatterBotType

app = Flask(__name__)

factory = ChatterBotFactory()

bot = factory.create(ChatterBotType.CLEVERBOT)
botsession = bot.create_session()

@app.route("/")
def hello():
    if request.method == 'GET':
        msg = request.args.get('msg', '');
        return botsession.think(msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
