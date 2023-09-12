import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return "☆ 𐎓⃝🌺🇲𝗼𝗻𝘀𝘁𝗲𝗿❤‍🔥⃟⃚⃐ 🌿 ☆ 

 ➪ 𝗣ɨɳɠ: 342.2 ᴍs 
 ➪ 𝗨թƬɨмє: 12m:16s 
 ➪ ⩔єяនɨ០ɳ: v0.6 ☆ Userbot is Up & Running!"

api.add_resource(Greeting, '/')
app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
