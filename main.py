import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("txtfiles/*txt")

pdf = FPDF(orientation="P", unit="mm", format="A4",)

for filepath in filepaths:
    with open(f'{filepath}') as file:
        data = file.readlines()
        pdf.add_page()
        filename = Path(filepath).stem
        name = filename.capitalize()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{name}")


pdf.output(f"PDFs/{filename}.pdf")
       
        
