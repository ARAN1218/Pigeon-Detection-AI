#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
import subprocess
import os

#Flaskオブジェクトの生成
app = Flask(__name__)

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = 'pigeon_app/static/media'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/index",methods=["post"])
def post():
    img_result = request.files['result']
    if img_result.filename == '':
        return render_template("index.html", img_result=False, error_flag=True)
    img_result.save(os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg'))
    subprocess.run(['python', 'pigeon_app/yolov5/detect.py', '--source', 'pigeon_app/static/media/result.jpg', '--weights', 'pigeon_app/yolov5/pigeon_5.pt', '--conf', '0.3', '--name', '../../../static/media', '--exist-ok'])
    return render_template("index.html", img_result=True)


if __name__ == "__main__":
    app.run(debug=True)