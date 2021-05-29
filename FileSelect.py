from SheetSelect import sheet_select
import pandas as pd
import tkinter as tk
import tkinter.filedialog


def file_select():
    # ---------------------------------------------------------------------------------------------------------------------------
    # 基のファイル選択ダイアログの表示
    root2 = tk.Tk()
    root2.title('File選択をしてください')

    fTyp = [("excel(.xlsm)", ".xlsm")]
    iDir = 'C://pg'
    file1 = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    # シートを取得
    root2.destroy()
    bk = pd.ExcelFile(file1)
    sheets = list(bk.sheet_names)
    selected = sheet_select(sheets)
    return selected, file1
