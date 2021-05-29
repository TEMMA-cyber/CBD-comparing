import tkinter as tk
from tkinter import ttk
import CostAnalysis
import pandas as pd

def re_cal(owner):
    global result
    result = CostAnalysis.data_scraping()
    label_name = ['file1_basic_information', 'file2_basic_information', 'file1_cost_information', 'file2_cost_information','difference_cost_information']
    for j, k in enumerate(label_name):
        for i in result[j]:
            label_widget = owner.nametowidget(f'!notebook.!frame.!main.{k}.labelframe_{i}.label_{i}')
            label_widget['text'] = result[j][i]

    scbox = owner.nametowidget(f'!notebook.!frame.!main.error_text')
    scbox.delete('1.0', 'end')
    scbox.insert('end', result[5])

# Upper===================================================================================================================
    upper_tree = owner.nametowidget(f'!notebook.!frame2.!upper.!frame{2}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[6]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame2.!upper.!frame{4}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[7]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame2.!upper.!frame{6}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[8]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame2.!upper.!frame{8}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[9]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

# Sole===================================================================================================================
    upper_tree = owner.nametowidget(f'!notebook.!frame3.!sole.!frame{2}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[10]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame3.!sole.!frame{4}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[11]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame3.!sole.!frame{6}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[12]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame3.!sole.!frame{8}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[13]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

# SolePaint===================================================================================================================
    upper_tree = owner.nametowidget(f'!notebook.!frame4.!solepaint.!frame{2}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[14]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame4.!solepaint.!frame{4}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[15]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame4.!solepaint.!frame{6}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[16]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame4.!solepaint.!frame{8}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[17]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

# Sundries===================================================================================================================
    upper_tree = owner.nametowidget(f'!notebook.!frame5.!sundries.!frame{2}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[18]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame5.!sundries.!frame{4}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[19]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame5.!sundries.!frame{6}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[20]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame5.!sundries.!frame{8}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[21]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))


# Sundries===================================================================================================================
    upper_tree = owner.nametowidget(f'!notebook.!frame6.!packing.!frame{2}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[22]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame6.!packing.!frame{4}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[23]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame6.!packing.!frame{6}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[24]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))

    upper_tree = owner.nametowidget(f'!notebook.!frame6.!packing.!frame{8}.!treeview')
    upper_tree.delete(*upper_tree.get_children())
    upper_result = result[25]

    for n in range(len(list(upper_result.index))):
        # データ挿入
        upper_tree.insert("", "end", values=(list(upper_result.iloc[n])))


def excel(owner):
    f_type = [('excel', '*.xlsx')]
    ini_dir = 'C://pg'
    ret = tk.filedialog.asksaveasfilename(defaultextension='xlsx', filetypes=f_type, initialdir=ini_dir,
                                               title='保存先を指定してください')
    Upper_cate = pd.concat([result[6],result[7],result[8],result[9]],sort=False)
    Sole_cate = pd.concat([result[10],result[11],result[12],result[13]],sort=False)
    SolePaint_cate = pd.concat([result[14],result[15],result[16],result[17]],sort=False)
    Sundries_cate = pd.concat([result[18],result[19],result[20],result[21]],sort=False)
    Packing_cate = pd.concat([result[22],result[23],result[24],result[25]],sort=False)

    with pd.ExcelWriter(ret) as writer:
        result[26].to_excel(writer, sheet_name='data1')
        result[27].to_excel(writer, sheet_name='data2')
        Upper_cate.to_excel(writer, sheet_name='Upper')
        Sole_cate.to_excel(writer, sheet_name='Sole')
        SolePaint_cate.to_excel(writer, sheet_name='Sole Paint')
        Sundries_cate.to_excel(writer, sheet_name='Sundries')
        Packing_cate.to_excel(writer, sheet_name='Packing')


def init_notebook(notebook):
    for name, tab_name, class_name in zip(['Main', 'Upper', 'Sole', 'Sole Paint', 'Sundries', 'Packing'],
                                          ['Main', 'Upper', 'Sole', 'Sole Paint', 'Sundries', 'Packing'],
                                          [Main, Upper, Sole, SolePaint, Sundries, Packing]):
        name = ttk.Frame(notebook)
        notebook.add(name, text=tab_name)
        class_name(master=name)

    return notebook


class ScrolledCanvas(tk.Canvas):

    def __init__(self, master, *args, **kw):
        super().__init__(master, *args, **kw)

        bar_y = ttk.Scrollbar(self, orient=tk.VERTICAL)
        bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        bar_y.config(command=self.yview)

        bar_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        bar_x.config(command=self.yview)

        self.config(
            yscrollcommand=bar_y.set,
            xscrollcommand=bar_x.set,
            scrollregion=(0,0,2000,2000),
        )


class MainWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        button = tk.Button(self, text='re-cal', command=lambda: re_cal(self))
        button.pack()
        button2 = tk.Button(self, text='xlsx_write', command=lambda: excel(self))
        button2.pack()

        canvas = ScrolledCanvas(self, width=1250)
        canvas.pack(fill=tk.BOTH, expand=True)  # <- 配置は利用側で決める

        notebook = init_notebook(ttk.Notebook(self))
        notebook.pack(fill=tk.BOTH, expand=True)

        canvas.create_window((0, 0),
                             window=notebook, anchor=tk.NW, width=canvas.cget('width'))

        self.canvas = canvas
        self.notebook = notebook


class Main(tk.Frame):
    global result
    result = CostAnalysis.data_scraping()

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self._MainCost_widget(result[0], 'File1 Basic information', 'file1_basic_information')
        self._MainCost_widget(result[1], 'File2 Basic information', 'file2_basic_information')
        self._MainCost_widget(result[2], 'File1 Cost information', 'file1_cost_information')
        self._MainCost_widget(result[3], 'File2 Cost information', 'file2_cost_information')
        self._MainCost_widget(result[4], 'Difference Cost information', 'difference_cost_information')
        self._warning_frame(result[5])

    def _MainCost_widget(self, cost_info, txt, txt2):
        a = tk.LabelFrame(self, text=txt, fg='Blue', name=txt2, font=('メイリオ', 10,'bold'), relief='raised',bd=5)
        a.pack(pady=10, anchor=tk.NW)

        for i in cost_info:
            b = tk.LabelFrame(a, text=i, bg='#fff', name=f'labelframe_{i}', relief='flat')
            c = tk.Label(b, text=cost_info[i], bg='#fff', name=f'label_{i}', font=('メイリオ', 10,'bold'))

            if txt == 'Difference Cost information':
                try:
                    float(c['text'])
                    c['fg'] = 'green'
                    print(float(c['text']) < float(0))
                    if float(c['text']) < float(0):
                        c['fg'] = 'red'
                    else:pass
                except ValueError:
                    pass
            else: pass
            b.pack(side=tk.LEFT,padx=5)
            c.pack(side=tk.LEFT)


    def _warning_frame(self, warning):
        scrolledtext = tk.Text(self, bg='white', fg='black', name='error_text')
        scrolledtext.configure(highlightbackground='red')
        scrolledtext.insert(tk.END, warning)
        scrolledtext.pack()


class Upper(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        upper_result = result[6:10]
        for i, name in enumerate(['Remove', 'Add', 'Changed point', 'Nothing Change']):
            self._result_frame(name, upper_result[i])

    def _result_frame(self, name, upper_result):
        remove = tk.Frame(self, relief='sunken',bd=5)
        remove_label = tk.Label(remove, text=name, font=('メイリオ', 10,'bold'))
        remove_frame = tk.Frame(self, bg='#fff')
        [widget.pack() for widget in (remove, remove_label)]
        remove_frame.pack(fill=tk.BOTH, expand=True)

        # Costの試算結果を表示するCanvasをとりあえず1パターンを作成してループに移行
        # Treeviewの作成
        tree = ttk.Treeview(remove_frame)
        tree["column"] = list(upper_result.columns)
        tree["show"] = "headings"

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

        for i in range(len(list(upper_result.columns))):
            tree.heading(upper_result.columns[i], text=upper_result.columns[i],
                         command=lambda _col=upper_result.columns[i]: treeview_sort_column(tree, _col, False))
            # 列の幅
            tree.column(upper_result.columns[i], width=30)
        for j in range(len(list(upper_result.index))):
            # データ挿入
            tree.insert("", "end", values=(list(upper_result.iloc[j])))

        # 設置
        tree.pack(fill=tk.BOTH, expand=True)


class Sole(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        upper_result = result[10:14]
        for i, name in enumerate(['Remove', 'Add', 'Changed point', 'Nothing Change']):
            self._result_frame(name, upper_result[i])

    def _result_frame(self, name, upper_result):
        remove = tk.Frame(self, relief='sunken',bd=5)
        remove_label = tk.Label(remove, text=name, font=('メイリオ', 10,'bold'))
        remove_frame = tk.Frame(self, bg='#fff')
        [widget.pack() for widget in (remove, remove_label)]
        remove_frame.pack(fill=tk.BOTH, expand=True)

        # Costの試算結果を表示するCanvasをとりあえず1パターンを作成してループに移行
        # Treeviewの作成
        tree = ttk.Treeview(remove_frame)
        tree["column"] = list(upper_result.columns)
        tree["show"] = "headings"

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

        for i in range(len(list(upper_result.columns))):
            tree.heading(upper_result.columns[i], text=upper_result.columns[i],
                         command=lambda _col=upper_result.columns[i]: treeview_sort_column(tree, _col, False))
            # 列の幅
            tree.column(upper_result.columns[i], width=30)
        for j in range(len(list(upper_result.index))):
            # データ挿入
            tree.insert("", "end", values=(list(upper_result.iloc[j])))

        # 設置
        tree.pack(fill=tk.BOTH, expand=True)


class SolePaint(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        upper_result = result[14:18]
        for i, name in enumerate(['Remove', 'Add', 'Changed point', 'Nothing Change']):
            self._result_frame(name, upper_result[i])

    def _result_frame(self, name, upper_result):
        remove = tk.Frame(self, relief='sunken',bd=5)
        remove_label = tk.Label(remove, text=name, font=('メイリオ', 10,'bold'))
        remove_frame = tk.Frame(self, bg='#fff')
        [widget.pack() for widget in (remove, remove_label)]
        remove_frame.pack(fill=tk.BOTH, expand=True)

        # Costの試算結果を表示するCanvasをとりあえず1パターンを作成してループに移行
        # Treeviewの作成
        tree = ttk.Treeview(remove_frame)
        tree["column"] = list(upper_result.columns)
        tree["show"] = "headings"

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

        for i in range(len(list(upper_result.columns))):
            tree.heading(upper_result.columns[i], text=upper_result.columns[i],
                         command=lambda _col=upper_result.columns[i]: treeview_sort_column(tree, _col, False))
            # 列の幅
            tree.column(upper_result.columns[i], width=30)
        for j in range(len(list(upper_result.index))):
            # データ挿入
            tree.insert("", "end", values=(list(upper_result.iloc[j])))

            # 設置
        tree.pack(fill=tk.BOTH, expand=True)


class Sundries(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        upper_result = result[18:22]
        for i, name in enumerate(['Remove', 'Add', 'Changed point', 'Nothing Change']):
            self._result_frame(name, upper_result[i])

    def _result_frame(self, name, upper_result):
        remove = tk.Frame(self, relief='sunken',bd=5)
        remove_label = tk.Label(remove, text=name, font=('メイリオ', 10,'bold'))
        remove_frame = tk.Frame(self, bg='#fff')
        [widget.pack() for widget in (remove, remove_label)]
        remove_frame.pack(fill=tk.BOTH, expand=True)

        # Costの試算結果を表示するCanvasをとりあえず1パターンを作成してループに移行
        # Treeviewの作成
        tree = ttk.Treeview(remove_frame)
        tree["column"] = list(upper_result.columns)
        tree["show"] = "headings"

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

        for i in range(len(list(upper_result.columns))):
            tree.heading(upper_result.columns[i], text=upper_result.columns[i],
                         command=lambda _col=upper_result.columns[i]: treeview_sort_column(tree, _col, False))
            # 列の幅
            tree.column(upper_result.columns[i], width=30)
        for j in range(len(list(upper_result.index))):
            # データ挿入
            tree.insert("", "end", values=(list(upper_result.iloc[j])))

        # 設置
        tree.pack(fill=tk.BOTH, expand=True)


class Packing(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        upper_result = result[22:26]
        for i, name in enumerate(['Remove', 'Add', 'Changed point', 'Nothing Change']):
            self._result_frame(name, upper_result[i])

    def _result_frame(self, name, upper_result):
        remove = tk.Frame(self, relief='sunken',bd=5)
        remove_label = tk.Label(remove, text=name, font=('メイリオ', 10,'bold'))
        remove_frame = tk.Frame(self, bg='#fff')
        [widget.pack() for widget in (remove, remove_label)]
        remove_frame.pack(fill=tk.BOTH, expand=True)

        # Costの試算結果を表示するCanvasをとりあえず1パターンを作成してループに移行
        # Treeviewの作成
        tree = ttk.Treeview(remove_frame)
        tree["column"] = list(upper_result.columns)
        tree["show"] = "headings"

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

        for i in range(len(list(upper_result.columns))):
            tree.heading(upper_result.columns[i], text=upper_result.columns[i], command=lambda _col=upper_result.columns[i]: treeview_sort_column(tree, _col, False))
            # 列の幅
            tree.column(upper_result.columns[i], width=30)
        for j in range(len(list(upper_result.index))):
            # データ挿入
            tree.insert("", "end", values=(list(upper_result.iloc[j])))

        # 設置conda
        tree.pack(fill=tk.BOTH, expand=True)


def main():
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("CBD Comparing")

    win = MainWindow(root)
    win.pack(fill='both', expand='YES')

    root.mainloop()


if __name__ == '__main__':
    main()
