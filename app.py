from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/upload", methods=['POST'])
def upload_file():
    file = request.files['file']
    input_img = Image.open(file.stream)
    output_img = remove(input_img, post_process_mask=True)
    img_io = BytesIO()
    output_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_rmbg.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5100)
