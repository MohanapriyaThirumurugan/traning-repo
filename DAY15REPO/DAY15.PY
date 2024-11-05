# FRONTEND URL

# https://github.com/MohanapriyaThirumurugan/photosep

# BACKEND
from flask import Flask, request, jsonify  
from flask_cors import CORS  
from PIL import Image  
import pytesseract  

class Service:
    def __init__(self, tesseract_path):
         pytesseract.pytesseract.tesseract_cmd = tesseract_path
    def extracimage(self, image_stream):
        try:
            image = Image.open(image_stream)

            extracted_text = pytesseract.image_to_string(image)
            return extracted_text
        except Exception as e:
             raise RuntimeError(f"Failed to extract text: {e}")

# Create a Flask app
app = Flask(__name__)
CORS(app)  

ocr_service = Service(tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected for uploading"}), 400
    try:
        extracted_text = ocr_service. extracimage(file.stream)
        
        return jsonify({"extracted_text": extracted_text})
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
