from flask import Flask, render_template, request, send_from_directory
import os
import uuid
from model import process_pdf_and_generate_report

app = Flask(__name__)

# Define the directory to save uploaded files and generated PDFs
UPLOAD_FOLDER = 'uploads'
GENERATED_PDFS_FOLDER = 'generated_pdfs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_PDFS_FOLDER'] = GENERATED_PDFS_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_PDFS_FOLDER, exist_ok=True)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the uploaded PDF and user text to generate the report
@app.route('/generate_report', methods=['POST'])
def generate_report():
    if 'pdf' not in request.files or 'user_text' not in request.form:
        return "Missing required inputs", 400

    file = request.files['pdf']
    user_text = request.form['user_text']

    if file.filename == '':
        return "No file selected", 400
    if file and file.filename.endswith('.pdf'):
        # Save the uploaded PDF
        file_id = str(uuid.uuid4())
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id + '.pdf')
        file.save(pdf_path)

        # Generate the report PDF
        generated_pdf_path = os.path.join(app.config['GENERATED_PDFS_FOLDER'], file_id + '_loan_report.pdf')
        loan_prediction = process_pdf_and_generate_report(pdf_path, user_text, generated_pdf_path)

        return render_template('result.html', pdf_filename=file_id + '_loan_report.pdf', loan_prediction=loan_prediction)

    return "Invalid file format. Only PDFs are allowed.", 400

# Route to download the generated PDF
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['GENERATED_PDFS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
