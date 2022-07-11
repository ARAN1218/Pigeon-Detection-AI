# 各種インポート
from flask import Flask,render_template,request
import subprocess
import os
from PIL import Image


# Flaskオブジェクトの生成
app = Flask(__name__)

# 画像のアップロードのための設定
UPLOAD_FOLDER = 'pigeon_app/static/media'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


# ホーム
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# 推論処理
@app.route("/index",methods=["post"])
def post():
    img_result = request.files['result']
    if img_result.filename == '':
        return render_template("index.html", img_result=False, error_flag=True)
    img_result.save(os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg'))
    subprocess.run(['python', 'pigeon_app/yolov5/detect.py', '--source', 'pigeon_app/static/media/result.jpg', '--weights', 'pigeon_app/yolov5/pigeon_5.pt', '--conf', '0.3', '--name', '../../../static/media', '--exist-ok'])
    img_result_share = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg'))
    img_result_share = img_result_share.resize((1200,630))
    img_result_share.save(os.path.join(app.config['UPLOAD_FOLDER'], 'result_share.jpg'))
    return render_template("index.html", img_result=True)


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/pigeons")
def pigeons():
    return render_template("pigeons.html")


@app.route("/tech")
def tech():
    return render_template("tech.html")

if __name__ == "__main__":
    app.run(debug=True)