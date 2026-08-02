import pandas as pd

# Use a raw string for Windows path to avoid escape-sequence errors
df = pd.read_excel(r"C:\Users\Public\Python\sctec_datviz_bi\praticas_python\Vendas - Dez.xlsx")

print(df.head())