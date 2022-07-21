import pandas as pd
from PyPDF2 import PdfReader

reader = PdfReader("projectile.pdf")
 
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)

# d = {"header":[data]}
# df = pd.DataFrame(data=d)``