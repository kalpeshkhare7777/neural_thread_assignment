# app.py

from flask import Flask, jsonify, send_file
from butterfly_gen import generate_butterfly_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CORS(app, origins='http://localhost:64488/')

@app.route('/refresh', methods=['GET'])
def refresh():
    save_path = "client/frontend/src/assets/images/butterfly.png"
    try:
        # Generate the butterfly image
        generate_butterfly_image(save_path)
        
        # Send the generated image back to the client
        return send_file(save_path, mimetype='image/png')
    except Exception as e:
        # If an error occurs during image generation, return an error response
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
