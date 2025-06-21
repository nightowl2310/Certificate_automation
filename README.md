Certificate Automation 🛠️🎓
Automate the generation of participation certificates from a single template and a list of participants!
This tool was created to efficiently generate 200+ certificates for the Summer Code Quest organized by GDGOC-IETDAVV, with GDGOC-IIPS and GDGOC-SDSF as marketing partners.


📁 Project Structure

CERTIFICATE_AUTOMATION/
│
├── Certificate_automation/            # (Optional) Source code folder
├── Certificate_automation.git/        # Git repository folder
├── output/                            # Generated certificates will be saved here
│
├── .gitignore                         # Git ignore rules
├── Certificate_template.png           # Certificate template image
├── generate_certificates.py           # Main automation script
├── Summer code quest registrations.xlsx # Excel file with participant data


🚀 Features
Generate personalized certificates from a single template
Read participant data from an Excel file
Output certificates automatically to the output/ directory



📝 Requirements
Python 3.x
Pillow (for image processing)
openpyxl (for reading Excel files)
Install dependencies: pip install pillow openpyxl


Usage
Prepare your files:
Place your certificate template image as Certificate_template.png.
Add your participant data in Summer code quest registrations.xlsx.

