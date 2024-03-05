import pandas as pd

def load(file):
    A = []
    B = []
    #xUnc = []
    yUnc = []
    file_name =  file +".xlsx"# path to file + file name
    df = pd.read_excel(io=file_name, sheet_name=0)
    data = df.values.tolist()
    for col in data:
        A += [float(col[0])]
        B += [float(col[1])]
        #yUnc += [float(col[2])]

    return A, B, yUnc