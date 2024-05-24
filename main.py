import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("txtfiles/*txt")

for filepath in filepaths:
    with open(f'{filepath}') as file:
        data = file.readlines()
        pdf = FPDF(orientation="P", unit="mm", format="A4",)
        get_title = data[0]
        pdf.add_page()
        filename = Path(filepath).stem
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{get_title}")
        pdf.output(f"PDFs/{filename}.pdf")
       
        
