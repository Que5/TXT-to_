import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("txtfiles/*txt")

pdf = FPDF(orientation="P", unit="mm", format="A4",)

for filepath in filepaths:
    with open(f'{filepath}') as file:
        data = file.read()
        pdf.add_page()
        filename = Path(filepath).stem
        name = filename.capitalize()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{name}", ln=1)
    
        
        pdf.set_font(family="Times", size=10)        
        pdf.multi_cell(w=0, h=6, txt=str(data))


pdf.output(f"PDFs/output.pdf")
       
        
