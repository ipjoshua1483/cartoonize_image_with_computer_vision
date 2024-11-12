from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from cartoonize import Cartoonize

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads/'  # Folder to store uploaded images
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32 MB limit
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}  # Allowed image types
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to upload the image
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an empty part without filename
        if file.filename == '':
            flash('Please upload an image')
            return redirect(request.url)
        
        # If file is allowed, save it
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_data = file.read()
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            cartoonize_obj = Cartoonize()
            cartoonize_obj.load_image(file_data)
            cartoonize_obj.save_image(filepath)
            cartoonize_obj.color_quantization()
            cartoonize_obj.bilateral_filter()
            cartoonize_obj.edge_mask()
            cartoonized_filename = f"cartoonized_{filename}"
            cartoonized_filepath = os.path.join(app.config['UPLOAD_FOLDER'], cartoonized_filename)
            cartoonize_obj.save_image(cartoonized_filepath, original = False)
            # return redirect(url_for('display_image', filename=cartoonized_filename))
            return redirect(
                url_for('display_images', 
                original_filename = filename, 
                cartoonized_filename = cartoonized_filename
                )
            )
    return render_template('upload.html')

@app.route('/display_images')
def display_images():
    original_filename = request.args.get('original_filename')
    cartoonized_filename = request.args.get('cartoonized_filename')
    return render_template(
        'display.html', 
        original_filename = original_filename,
        cartoonized_filename = cartoonized_filename,
    )

if __name__ == "__main__":
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug = False)