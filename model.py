import fitz  # PyMuPDF
import openai
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# OpenAI API key
openai.api_key = "YOUR_API_KEY"
# Function to extract text from the PDF
def extract_text_from_pdf(pdf_file):
    # Open the PDF with PyMuPDF
    doc = fitz.open(pdf_file)
    pdf_text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        pdf_text += page.get_text("text")
    return pdf_text

# Function to predict loan and repayment period based on extracted text and user input
def predict_loan_and_repayment_period(pdf_text, user_text):
    # The rest of the function remains the same
    prompt = f"""
    Based on the following financial data extracted from a PDF, predict how much loan the person can take and the repayment period. Consider their income, expenses, and any other relevant financial data from the text:

    {pdf_text}

    {user_text}

    Consider the person's available monthly income after expenses, and calculate:
    1. The loan amount they can afford, assuming they can repay 30% of their available income monthly.
    2. The repayment period in years, based on typical interest rates (5-8%) for personal loans.

    Output the result as:
    "The amount this person can take loan in INR is X and repay it in Y years,this person can have to pay Z amount per month for Y years/months along with interest."
    """

    # Use OpenAI API to predict loan and repayment period
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": "You are a financial assistant of an Indian labour person. Your task is to provide the maximum loan amount a person can take, the duration (in months/years/days) over which it can be repaid, and the monthly payment amount including interest. Do not provide suggestions, request extra details, or summarize information. Just output the loan amount, repayment period, and monthly payment with interest,and also predict a risk score based on observation from 0-100 dont ask anything more and first give the risk score then give the other details ..and also make a recommendation ,a roadmap type what this person should do have a good money in future and what to do to income more as a vendor .."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    # Extract the loan prediction result
    loan_prediction = response['choices'][0]['message']['content'].strip()
    return loan_prediction

# Function to create a PDF with the loan prediction
def create_pdf_with_loan_prediction(filename, logo_path, loan_prediction):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # A4 dimensions
    c.setFillColor(colors.HexColor("#4272F4"))
    c.rect(0, height - 50, width, 50, stroke=0, fill=1)

    # Add logo to top left corner
    logo_size = 40
    c.drawImage(logo_path, 10, height - 50 + (50 - logo_size) / 2, width=logo_size, height=logo_size, mask='auto')

    # Add header text
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, height - 35, "Cred-Arth Prediction Report")

    # Add title
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(30, height - 100, "Financial Loan Analysis")

    # Add a separator line
    c.setStrokeColor(colors.HexColor("#4272F4"))
    c.setLineWidth(2)
    c.line(30, height - 110, width - 30, height - 110)

    # Add loan prediction content
    margin_left = 30
    margin_right = width - 30
    y_position = height - 150
    line_height = 16

    c.setFont("Helvetica", 12)
    lines = loan_prediction.split("\n")
    for line in lines:
        words = line.split()
        current_line = ""
        for word in words:
            test_line = f"{current_line} {word}".strip()
            if c.stringWidth(test_line, "Helvetica", 12) < (margin_right - margin_left):
                current_line = test_line
            else:
                c.drawString(margin_left, y_position, current_line)
                y_position -= line_height
                current_line = word

            if y_position < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 50

        if current_line:
            c.drawString(margin_left, y_position, current_line)
            y_position -= line_height

    # Footer
    c.setFillColor(colors.HexColor("#888888"))
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(30, 30, "© 2024 Financial Report. All rights reserved by CredArth.")
    c.drawString(20, 20, "      Made By Team DDC BADMOS With Love in ICDMAI Hackathon 2024")

    c.save()

# Main function to process the uploaded PDF and generate the report
def process_pdf_and_generate_report(pdf_file, user_text, generated_pdf_path):
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_file)
    
    # Predict loan and repayment period based on extracted PDF text and user input
    loan_prediction = predict_loan_and_repayment_period(pdf_text, user_text)
    
    # Create a PDF with the loan prediction
    create_pdf_with_loan_prediction(generated_pdf_path, 'WhatsApp Image 2024-12-19 at 17.53.05.jpeg', loan_prediction)
    
    return loan_prediction
