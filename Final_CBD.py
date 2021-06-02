import pandas as pd
import tkinter as tk
import FileSelect
import CostAnalysis
import tkinter.ttk as ttk
import tkinter.scrolledtext as tksc

sheet_name1, file1 = FileSelect.file_select()
sheet_name2, file2 = FileSelect.file_select()
# print(sheet_name1, file1, sheet_name2, file2)
# 2つの比較するファイルの読み込み
df1 = pd.read_excel(file1, sheet_name=sheet_name1, header=None)
df2 = pd.read_excel(file2, sheet_name=sheet_name2, header=None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)
# モデルの基本情報とコストの基本情報の取得
BasicInformation1 = {"Plan_No.": df1.iat[1, 4], "Nick name": df1.iat[2, 10], "Stage": df1.iat[3, 4],
                     "Season": df1.iat[1, 8], "Forecast": df1.iat[5, 8], "Target FOB": df1.iat[5, 10]}
BasicInformation2 = {"Plan_No.": df2.iat[1, 4], "Nick name": df2.iat[2, 10], "Stage": df2.iat[3, 4],
                     "Season": df2.iat[1, 8], "Forecast": df2.iat[5, 8], "Target FOB": df2.iat[5, 10]}
print(BasicInformation1)
print(BasicInformation2)
# シューズコストの差し引き
MainCostInformation1 = {"Upper Material": df1.iat[9, 5], "Sole Material": df1.iat[10, 5],
                        "Other Material": df1.iat[11, 5], "LO": df1.iat[12, 5], "Profit": df1.iat[13, 5],
                        "Net FOB": df1.iat[14, 5], "Adjustment": df1.iat[15, 5], "CFM FOB": df1.iat[16, 5],
                        "Direct Labor": df1.iat[13, 10], "Over-head": df1.iat[14, 10],
                        "Profit Value": df1.iat[9, 14]}
MainCostInformation2 = {"Upper Material": df2.iat[9, 5], "Sole Material": df2.iat[10, 5],
                        "Other Material": df2.iat[11, 5], "LO": df2.iat[12, 5], "Profit": df2.iat[13, 5],
                        "Net FOB": df2.iat[14, 5], "Adjustment": df2.iat[15, 5], "CFM FOB": df2.iat[16, 5],
                        "Direct Labor": df2.iat[13, 10], "Over-head": df2.iat[14, 10],
                        "Profit Value": df2.iat[9, 14]}
MainCostDifference = {}
for i in MainCostInformation1:
    MainCostDifference[i] = MainCostInformation1[i] - MainCostInformation2[i]
print(MainCostDifference)

Upper1ON, Upper2ON, UpperDP, UpperNC, UpperSum1, UpperSum2 = CostAnalysis.cost_cal(df1, df2, 25, 127)
Sole1ON, Sole2ON, SoleDP, SoleNC, SoleSum1, SoleSum2 = CostAnalysis.cost_cal(df1, df2, 132, 149)
SolePaint1ON, SolePaint2ON, SolePaintDP, SolePaintNC, SolePaintSum1, SolePaintSum2 = CostAnalysis.cost_cal(df1, df2,
                                                                                                           154, 166)
Sundries1ON, Sundries2ON, SundriesDP, SundriesNC, SundriesSum1, SundriesSum2 = CostAnalysis.cost_cal(df1, df2, 170, 182)
Packing1ON, Packing2ON, PackingDP, PackingNC, PackingSum1, PackingSum2 = CostAnalysis.cost_cal(df1, df2, 187, 210)

sumlist1 = [UpperSum1, SoleSum1, SolePaintSum1, SundriesSum1, PackingSum1]
sumlist2 = [UpperSum2, SoleSum2, SolePaintSum2, SundriesSum2, PackingSum2]
for s, t, u, in zip(sumlist1, [126, 148, 165, 181, 209],
                    ['UpperSum1', 'SoleSum1', 'SolePaintSum1', 'SundriesSum1', 'PackingSum1']):
    if s == df1.iat[t, 23]:
        print('calculation of ' + u + ' is correct')
        print(s, df1.iat[t, 23])
    else:
        print('calculation of ' + u + ' is wrong')
        print(s, df1.iat[t, 23])

for s, t, u, in zip(sumlist2, [126, 148, 165, 181, 209],
                    ['UpperSum2', 'SoleSum2', 'SolePaintSum2', 'SundriesSum2', 'PackingSum2']):
    if s == df2.iat[t, 23]:
        print('calculation of ' + u + ' is correct')
        print(s, df2.iat[t, 23])
    else:
        print('calculation of ' + u + ' is wrong')
        print(s, df2.iat[t, 23])

Upper1ON = Upper1ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
Upper2ON = Upper2ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
UpperNC = UpperNC.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)

SolePaint1ON = SolePaint1ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
SolePaint2ON = SolePaint2ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
SolePaintNC = SolePaintNC.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)

Sole1ON = Sole1ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
Sole2ON = Sole2ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
SoleNC = SoleNC.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)

Sundries1ON = Sundries1ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
Sundries2ON = Sundries2ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
SundriesNC = SundriesNC.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)

Packing1ON = Packing1ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
Packing2ON = Packing2ON.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)
PackingNC = PackingNC.drop(['count', 'none2', 'none3', 'none4', 'none5'], axis=1)

Upper = pd.concat([Upper1ON, Upper2ON, UpperDP, UpperNC], sort=False)
Sole = pd.concat([Sole1ON, Sole2ON, SoleDP, SoleNC], sort=False)
SolePaint = pd.concat([SolePaint1ON, SolePaint2ON, SolePaintDP, SolePaintNC], sort=False)
Sundries = pd.concat([Sundries1ON, Sundries2ON, SundriesDP, SundriesNC], sort=False)
Packing = pd.concat([Packing1ON, Packing2ON, PackingDP, PackingNC], sort=False)

with pd.ExcelWriter('C:/Users/VAIO-L/Desktop/pandas_to_excel_multi4.xlsx') as writer:
    Upper.to_excel(writer, sheet_name='Upper')
    Sole.to_excel(writer, sheet_name='Sole')
    SolePaint.to_excel(writer, sheet_name='Sole Paint')
    Sundries.to_excel(writer, sheet_name='Sundries')
    Packing.to_excel(writer, sheet_name='Packing')


# ----------------------------------------------------------------------------------------------------------------------------
# GUIの作成
root = tk.Tk()
root.geometry('2000x1500')
root.title('CBD比較のやつ')

# Canvas Widget を生成
canvas = tk.Canvas(root, width=2000, height=1500)

# Scrollbar を生成して配置
bar_y = tk.Scrollbar(root, orient=tk.VERTICAL)
bar_y.pack(side=tk.RIGHT, fill=tk.Y)
bar_y.config(command=canvas.yview)

bar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
bar_x.pack(side=tk.BOTTOM, fill=tk.X)
bar_x.config(command=canvas.xview)

# Canvas Widget を配置
canvas.config(yscrollcommand=bar_y.set, xscrollcommand=bar_x.set)
canvas.config(scrollregion=(0, 0, 4000, 5000))  # スクロール範囲
canvas.pack(fill=tk.BOTH, expand=tk.YES)

# Frame Widgetを 生成
frame = tk.Frame(canvas)

# Frame Widgetを Canvas Widget上に配置
canvas.create_window((0, 0), window=frame, anchor=tk.NW, width=canvas.cget('width'))

notebook = ttk.Notebook(frame)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
tab4 = tk.Frame(notebook)
tab5 = tk.Frame(notebook)
tab6 = tk.Frame(notebook)

notebook.add(tab1, text='main')
notebook.add(tab2, text='Upper')
notebook.add(tab3, text='Sole')
notebook.add(tab4, text='Sole Paint')
notebook.add(tab5, text='Sundries')
notebook.add(tab6, text='Packing')
notebook.pack(expand=True, fill='both')

# main
# ファイル情報と基本的なコスト情報
# FILE１に入っているメインの情報を入れるLabelFrameを作成
# CBD基本情報
frame_file1 = tk.LabelFrame(tab1, text='File1 Basic information', width=1200, height=200, bg='#fff', fg='Blue')
frame_file1.pack(pady=10, anchor=tk.NW)

for i in BasicInformation1:
    b = tk.LabelFrame(frame_file1, text=i, bg='#fff')
    c = tk.Label(b, text=BasicInformation1[i], bg='#fff')
    [widget.pack(side=tk.LEFT) for widget in (b, c)]

# Main Cost Information
frame_cost_file1 = tk.LabelFrame(tab1, text='File1 Cost information', width=1200, height=200, bg='#fff', fg='Blue')
frame_cost_file1.pack(pady=10, anchor=tk.NW)

for i in MainCostInformation1:
    b = tk.LabelFrame(frame_cost_file1, text=i, bg='#fff')
    c = tk.Label(b, text=MainCostInformation1[i], bg='#fff')
    [widget.pack(side=tk.LEFT) for widget in (b, c)]

# FILE2に入っているメインの情報を入れるLabelFrameを作成
# CBD基本情報
frame_file2 = tk.LabelFrame(tab1, text='File2 Basic Information', width=1200, height=200, bg='#fff', fg='Blue')
frame_file2.pack(pady=20, anchor=tk.NW)

for i in BasicInformation2:
    b = tk.LabelFrame(frame_file2, text=i, bg='#fff')
    c = tk.Label(b, text=BasicInformation2[i], bg='#fff')
    [widget.pack(side=tk.LEFT) for widget in (b, c)]

# Main Cost Information
frame_cost_file2 = tk.LabelFrame(tab1, text='File2 Cost information', width=1200, height=200, bg='#fff', fg='Blue')
frame_cost_file2.pack(pady=10, anchor=tk.NW)

for i in MainCostInformation2:
    b = tk.LabelFrame(frame_cost_file2, text=i, bg='#fff')
    c = tk.Label(b, text=MainCostInformation2[i], bg='#fff')
    [widget.pack(side=tk.LEFT) for widget in (b, c)]

# Difference Costを表示
frame_cost = tk.LabelFrame(tab1, text='Main Cost Difference', width=1200, height=200, bg='#fff', fg='Blue')
frame_cost.pack(pady=10, anchor=tk.NW)

for i in MainCostDifference:
    b = tk.LabelFrame(frame_cost, text=i, bg='#fff')
    c = tk.Label(b, text=MainCostDifference[i], bg='#fff')
    [widget.pack(side=tk.LEFT) for widget in (b, c)]

# Mainに入れる検算結果
scrolledtext = tksc.ScrolledText(tab1, height=20, width=200)
scrolledtext.insert(tk.END, 'ここに価格の検算をインサートする')
scrolledtext.pack()

# -----------------------------------------------------------------------------------------------------
# Upperの計算結果を表示
Upper_cate = [Upper1ON, Upper2ON, UpperDP, UpperNC]
Sole_cate = [Sole1ON, Sole2ON, SoleDP, SoleNC]
SolePaint_cate = [SolePaint1ON, SolePaint2ON, SolePaintDP, SolePaintNC]
Sundries_cate = [Sundries1ON, Sundries2ON, SundriesDP, SundriesNC]
Packing_cate = [Packing1ON, Packing2ON, PackingDP, PackingNC]
for tab, cate in zip([tab2, tab3, tab4, tab5, tab6], [Upper_cate, Sole_cate, SolePaint_cate, Sundries_cate, Packing_cate]):
    remove = tk.Frame(tab, width=1200, height=10)
    remove_label = tk.Label(remove, text='Remove')
    upper_remove_frame = tk.Frame(tab, bg='#fff', width=1200, height=200)
    add = tk.Frame(tab, width=1200, height=10)
    add_label = tk.Label(add, text='Add')
    upper_add_frame = tk.Frame(tab, bg='red', width=1200, height=200)
    different = tk.Frame(tab, width=1200, height=10)
    different_label = tk.Label(different, text='Changed point')
    upper_change_frame = tk.Frame(tab, bg='#fff', width=1200, height=200)
    nochange = tk.Frame(tab, width=1200, height=10)
    nochange_label = tk.Label(nochange, text='Nothing Change')
    upper_same_frame = tk.Frame(tab, bg='#fff', width=1200, height=200)

    [widget.pack() for widget in (remove, remove_label, upper_remove_frame, add, add_label, upper_add_frame
                                  , different, different_label, upper_change_frame, nochange, nochange_label, upper_same_frame, )]

    for name, name2 in zip([upper_remove_frame, upper_add_frame, upper_change_frame, upper_same_frame], cate):
        # Costの試算結果を表示するCanvasをとりあえず1パターンを作成してループに移行
        canvas = tk.Canvas(name, width=2000, height=200)
        # Scrollbar を生成して配置
        bar_y = tk.Scrollbar(name, orient=tk.VERTICAL)
        bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        bar_y.config(command=canvas.yview)

        bar_x = tk.Scrollbar(name, orient=tk.HORIZONTAL)
        bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        bar_x.config(command=canvas.xview)

        # Treeviewの作成
        tree = ttk.Treeview(canvas)
        tree["column"] = list(name2.columns)
        tree["show"] = "headings"
        #ヘッダーテキスト

        for i in range(len(list(name2.columns))):
            tree.heading(name2.columns[i], text=name2.columns[i])
            #列の幅
            tree.column(name2.columns[i], width=50)
        for j in range(len(list(name2.index))):
            #データ挿入
            tree.insert("", "end", values=(list(name2.iloc[j])))

        #設置
        tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Canvas Widget を配置
        canvas.config(yscrollcommand=bar_y.set, xscrollcommand=bar_x.set)
        canvas.config(scrollregion=(0, 0, 4000, 5000))  # スクロール範囲
        canvas.create_window((0, 0), window=tree, anchor=tk.NW, width=canvas.cget('width'))
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# --------------------------------------------------------------------------------------------------------------------------
root.mainloop()