def cost_cal(df1, df2, row1, row2):
    import pandas as pd

    Upper1 = pd.DataFrame(df1.iloc[row1:row2, 3:24])
    Upper1.columns = ['Parts Name', "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                      "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount", "Tariff",
                      "Adjustment",
                      "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage", "Price per Pair(USD)"]
    Upper1 = Upper1.set_index('Parts Name')
    Upper1 = Upper1.reset_index()

    Upper2 = pd.DataFrame(df2.iloc[row1:row2, 3:24])
    Upper2.columns = ["Parts Name", "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                      "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount", "Tariff",
                      "Adjustment",
                      "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage", "Price per Pair(USD)"]
    Upper2 = Upper2.set_index('Parts Name')
    Upper2 = Upper2.reset_index()

    # Parts Nameの比較
    length = range(len(list(Upper1.index)))
    Del1 = []
    Del2 = []
    # Material Name / Parts Name が空欄の行を削除する
    for i in length:
        if str(Upper1.iloc[i, 0]) == 'nan':
            Del1.append(i)
        elif str(Upper1.iat[i, 9]) == 'nan':
            Del1.append(i)
        if str(Upper2.iloc[i, 0]) == 'nan':
            Del2.append(i)
        elif str(Upper2.iat[i, 9]) == 'nan':
            Del2.append(i)

    Upper1 = Upper1.drop(Del1)
    Upper2 = Upper2.drop(Del2)
    Upper1 = Upper1.reset_index()
    Upper2 = Upper2.reset_index()
    Upper1 = Upper1.drop(Upper1.columns[0], axis=1)
    Upper2 = Upper2.drop(Upper2.columns[0], axis=1)
    Upper1['count'] = Upper1.groupby('Parts Name').cumcount() + 1
    Upper2['count'] = Upper2.groupby('Parts Name').cumcount() + 1
    # ここまでOK

    # コスト比較をPats Nameごとに算出し抽出する
    # Upper1にあってUpper2に無いものを抽出
    UpperDiffInfo = pd.DataFrame(
        columns=["Material Name", "Supplier Name", "Unit of Measure", "Total Price(USD)", "Net Usage", "Waste%"])

    Upper1Only = pd.DataFrame(
        columns=["Parts Name", "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                 "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount",
                 "Tariff",
                 "Adjustment",
                 "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage",
                 "Price per Pair(USD)"])
    Upper2Only = pd.DataFrame(
        pd.DataFrame(
            columns=["Parts Name", "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                     "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount", "Tariff",
                     "Adjustment",
                     "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage",
                     "Price per Pair(USD)"]))
    Del1.clear()
    Del2.clear()

    # 完全一致しているものの抽出
    NothingChange = pd.DataFrame(
        pd.DataFrame(
            columns=['Parts Name', "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                     "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount", "Tariff",
                     "Adjustment",
                     "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage",
                     "Price per Pair(USD)"]))

    length1 = range(len(list(Upper1.index)))
    length2 = range(len(list(Upper2.index)))
    for i in length1:
        # 同じParts name同士の項目が完全に一致するならばインデックスを'DEL'に変えてNothing changeの箱に入れる　→　残りはどこかの項目が異なる同じParts nameか独自のParts name
        for j in length2:
            if list(Upper1.iloc[i]) == list(Upper2.iloc[j]):
                if Upper1.iloc[i, 0] not in NothingChange.index:
                    NothingChange.loc[Upper1.iloc[i, 0]] = Upper1.iloc[i] # 同じ名前の項目があると上書きされてしまう。
                    Upper1 = Upper1.rename(index={list(Upper1.index)[i]: 'DEL'})
                    Upper2 = Upper2.rename(index={list(Upper2.index)[j]: 'DEL'})
                    # print(Upper1.iloc[i, 0] + ' is Nothing Changed')

                elif Upper1.iloc[i, 0] in NothingChange.index:
                    NothingChange.loc[Upper1.iloc[i, 0]+str(2)] = Upper1.iloc[i] # 同じ名前の項目があると上書きされてしまう。
                    Upper1 = Upper1.rename(index={list(Upper1.index)[i]: 'DEL'})
                    Upper2 = Upper2.rename(index={list(Upper2.index)[j]: 'DEL'})
                    # print(Upper1.iloc[i, 0] + ' is Nothing Changed')
            else:
                pass
    NothingChange = NothingChange.reset_index()
    NothingChange = NothingChange.drop(NothingChange.columns[0], axis=1)
    # 上のブロックで抽出した完全一致している行をUpperの箱から削除
    if 'DEL' in list(Upper1.index):
        Upper1 = Upper1.drop('DEL', axis=0)
    else:
        pass

    if 'DEL' in list(Upper2.index):
        Upper2 = Upper2.drop('DEL', axis=0)
    else:
        pass

    # Upper1のParts NameにはあるけどUpper2のParts Nameには入っていないものを抽出（Upper2 <= Upper1もやる）　抽出されたParts NameはUpperの箱から削除する
    # そもそもParts Nameがどちらかにしかないものを抽出してそれをUpperの箱から削除
    Upper1Only = Upper1[~Upper1['Parts Name'].isin(Upper2['Parts Name'])]
    Upper2Only = Upper2[~Upper2['Parts Name'].isin(Upper1['Parts Name'])]
    Upper1 = Upper1[~Upper1['Parts Name'].isin(Upper1Only['Parts Name'])]
    Upper2 = Upper2[~Upper2['Parts Name'].isin(Upper2Only['Parts Name'])]

    # 同じParts NameだけどCountが異なるもので片方にしかないものを抽出してOnlyの箱に追加
    length1 = range(len(list(Upper1.index)))
    length2 = range(len(list(Upper2.index)))
    length3 = range(len(list(Upper2.columns)))

    DifferencePoint = pd.DataFrame(
        pd.DataFrame(columns=['Parts Name', 'Change Item', 'file1', 'file2',
                              'Difference Cost']))

    DifferenceCost1 = pd.DataFrame(
        pd.DataFrame(
            columns=['Parts Name', "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                     "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount", "Tariff",
                     "Adjustment",
                     "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage",
                     "Price per Pair(USD)"]))

    DifferenceCost2 = pd.DataFrame(
        pd.DataFrame(
            columns=['Parts Name', "count", "Material Name", "none2", "none3", "none4", "Supplier Name", "none5",
                     "Pantone code", "Unit of Measure", "Local Currency", "Unit Price", "Discount", "Tariff",
                     "Adjustment",
                     "Total Price", "Total Price(USD)", "Net Usage", "Waste%", "Adjust Usage",
                     "Price per Pair(USD)"]))

    for i in length1:
        for j in length2:
            if Upper1.iloc[i, 0] == Upper2.iloc[j, 0] and Upper1.iloc[i, 1] == Upper2.iloc[j, 1]:
                DifferenceCost1.loc[Upper1.iloc[i, 0]] = Upper1.iloc[i]
                DifferenceCost2.loc[Upper2.iloc[j, 0]] = Upper2.iloc[j]
                for k in length3:
                    if str(Upper1.iloc[i, k]) != str(Upper2.iloc[j, k]):
                        DifferencePoint.loc[Upper1.iloc[i, 0]] = [Upper1.iloc[i, 0], Upper1.columns[k],
                                                                  Upper1.iloc[i, k], Upper2.iloc[j, k], 'nan']
                        # print(Upper1.iloc[i, 0], Upper1.columns[k], Upper1.iloc[i, k], Upper2.iloc[j, k])
                        # if k == 20:
                        CostDiff = round(Upper2.iloc[j, 20] - Upper1.iloc[i, 20],3)
                        DifferencePoint.loc[Upper1.iloc[i, 0], 'Difference Cost'] = CostDiff
                        # print(CostDiff)
                Upper1 = Upper1.rename(index={list(Upper1.index)[i]: 'DEL'})
                Upper2 = Upper2.rename(index={list(Upper2.index)[j]: 'DEL'})

    DifferencePoint = DifferencePoint.reset_index()
    DifferencePoint = DifferencePoint.drop(DifferencePoint.columns[0], axis=1)
    DifferenceCost1 = DifferenceCost1.reset_index()
    DifferenceCost1 = DifferenceCost1.drop(DifferenceCost1.columns[0], axis=1)
    DifferenceCost2 = DifferenceCost2.reset_index()
    DifferenceCost2 = DifferenceCost2.drop(DifferenceCost2.columns[0], axis=1)

    # 上のブロックで抽出した完全一致している行をUpperの箱から削除
    if 'DEL' in list(Upper1.index):
        Upper1 = Upper1.drop('DEL', axis=0)
    else:
        pass

    if 'DEL' in list(Upper2.index):
        Upper2 = Upper2.drop('DEL', axis=0)
    else:
        pass

    if not Upper1.empty:
        Upper1Only = pd.concat([Upper1Only, Upper1])

    if not Upper2.empty:
        Upper2Only = pd.concat([Upper2Only, Upper2])

    CostSum1 = sum(DifferenceCost1['Price per Pair(USD)']) + sum(NothingChange['Price per Pair(USD)']) + sum(Upper1Only['Price per Pair(USD)'])
    CostSum2 = sum(DifferenceCost2['Price per Pair(USD)']) + sum(NothingChange['Price per Pair(USD)']) + sum(Upper2Only['Price per Pair(USD)'])

    return Upper1Only, Upper2Only, DifferencePoint, NothingChange, CostSum1, CostSum2

# -------------------------------------------------------------------------------------------------------------------------------------

def data_scraping():
    import pandas as pd
    import FileSelect
    import CostAnalysis

    sheet_name1, file1 = FileSelect.file_select()
    sheet_name2, file2 = FileSelect.file_select()
    # print(sheet_name1, file1, sheet_name2, file2)
    # 2つの比較するファイルの読み込み
    df1 = pd.read_excel(file1, sheet_name=sheet_name1, header=None)
    df2 = pd.read_excel(file2, sheet_name=sheet_name2, header=None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_column', None)

    for i in range(25,127):
        df1.iat[i,23] = round(df1.iat[i,23],3)
        df2.iat[i, 23] = round(df2.iat[i, 23], 3)
        df1.iat[i,22] = round(df1.iat[i,22],3)
        df2.iat[i, 22] = round(df2.iat[i, 22], 3)
    for i in range(132,149):
        df1.iat[i,23] = round(df1.iat[i,23],3)
        df2.iat[i, 23] = round(df2.iat[i, 23], 3)
        df1.iat[i, 22] = round(df1.iat[i, 22], 3)
        df2.iat[i, 22] = round(df2.iat[i, 22], 3)
    for i in range(154,166):
        df1.iat[i,23] = round(df1.iat[i,23],3)
        df2.iat[i, 23] = round(df2.iat[i, 23], 3)
        df1.iat[i, 22] = round(df1.iat[i, 22], 3)
        df2.iat[i, 22] = round(df2.iat[i, 22], 3)
    for i in range(170,182):
        df1.iat[i,23] = round(df1.iat[i,23],3)
        df2.iat[i, 23] = round(df2.iat[i, 23], 3)
        df1.iat[i, 22] = round(df1.iat[i, 22], 3)
        df2.iat[i, 22] = round(df2.iat[i, 22], 3)
    for i in range(187,210):
        df1.iat[i,23] = round(df1.iat[i,23],3)
        df2.iat[i, 23] = round(df2.iat[i, 23], 3)
        df1.iat[i, 22] = round(df1.iat[i, 22], 3)
        df2.iat[i, 22] = round(df2.iat[i, 22], 3)

    # モデルの基本情報とコストの基本情報の取得
    BasicInformation1 = {"Plan_No": df1.iat[1, 4], "Color_No": df1.iat[1, 6], "Nick name": df1.iat[2, 10], "Stage": df1.iat[3, 4],
                         "Season": df1.iat[1, 8], "Forecast": df1.iat[5, 8], "Target FOB": df1.iat[5, 10]}
    BasicInformation2 = {"Plan_No": df2.iat[1, 4], "Color_No": df2.iat[1, 6], "Nick name": df2.iat[2, 10], "Stage": df2.iat[3, 4],
                         "Season": df2.iat[1, 8], "Forecast": df2.iat[5, 8], "Target FOB": df2.iat[5, 10]}

    # シューズコストの差し引き
    MainCostInformation1 = {"Upper Material": round(df1.iat[9, 5],3), "Sole Material": round(df1.iat[10, 5],3),
                            "Other Material": round(df1.iat[11, 5],3), "LO": round(df1.iat[12, 5],3), "Profit": round(df1.iat[13, 5],3),
                            "Net FOB": round(df1.iat[14, 5],3), "Adjustment": round(df1.iat[15, 5],3), "CFM FOB": round(df1.iat[16, 5],3),
                            "Direct Labor": round(df1.iat[13, 10],3), "Over-head": round(df1.iat[14, 10],3),
                            "Profit Value": round(df1.iat[9, 14],3)}
    MainCostInformation2 = {"Upper Material": round(df2.iat[9, 5],3), "Sole Material": round(df2.iat[10, 5],3),
                            "Other Material": round(df2.iat[11, 5],3), "LO": round(df2.iat[12, 5],3), "Profit": round(df2.iat[13, 5],3),
                            "Net FOB": round(df2.iat[14, 5],3), "Adjustment": round(df2.iat[15, 5],3), "CFM FOB": round(df2.iat[16, 5],3),
                            "Direct Labor": round(df2.iat[13, 10],3), "Over-head": round(df2.iat[14, 10],3),
                            "Profit Value": round(df2.iat[9, 14],3)}
    MainCostDifference = {}

    for i in MainCostInformation1:
        MainCostDifference[i] = round(MainCostInformation2[i] - MainCostInformation1[i],3)

    Upper1ON, Upper2ON, UpperDP, UpperNC, UpperSum1, UpperSum2 = CostAnalysis.cost_cal(df1, df2, 25, 126)
    Sole1ON, Sole2ON, SoleDP, SoleNC, SoleSum1, SoleSum2 = CostAnalysis.cost_cal(df1, df2, 132, 148)
    SolePaint1ON, SolePaint2ON, SolePaintDP, SolePaintNC, SolePaintSum1, SolePaintSum2 = CostAnalysis.cost_cal(df1, df2,
                                                                                                               153, 165)
    Sundries1ON, Sundries2ON, SundriesDP, SundriesNC, SundriesSum1, SundriesSum2 = CostAnalysis.cost_cal(df1, df2, 169,
                                                                                                         181)
    Packing1ON, Packing2ON, PackingDP, PackingNC, PackingSum1, PackingSum2 = CostAnalysis.cost_cal(df1, df2, 186, 209)

    sumlist1 = [UpperSum1, SoleSum1, SolePaintSum1, SundriesSum1, PackingSum1]
    sumlist2 = [UpperSum2, SoleSum2, SolePaintSum2, SundriesSum2, PackingSum2]

    warning_list = []
    for s, t, u, in zip(sumlist1, [126, 148, 165, 181, 209],
                        ['UpperSum1', 'SoleSum1', 'SolePaintSum1', 'SundriesSum1', 'PackingSum1']):
        if s == df1.iat[t, 23]:
            warning_list.append('\ncalculation of ' + u + ' is correct')
            warning_list.append(str(round(s,3)) + '   ' + str(round(df1.iat[t, 23],3)))
        else:
            warning_list.append('\ncalculation of ' + u + ' is wrong')
            warning_list.append(str(round(s,3)) + '   ' + str(round(df1.iat[t, 23],3)))

    for s, t, u, in zip(sumlist2, [126, 148, 165, 181, 209],
                        ['UpperSum2', 'SoleSum2', 'SolePaintSum2', 'SundriesSum2', 'PackingSum2']):
        if s == df2.iat[t, 23]:
            warning_list.append('\ncalculation of ' + u + ' is correct')
            warning_list.append(str(round(s,3)) + '   ' + str(round(df2.iat[t, 23],3)))
        else:
            warning_list.append('\ncalculation of ' + u + ' is wrong')
            warning_list.append(str(round(s,3)) + '   ' + str(round(df2.iat[t, 23],3)))

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

    return ([BasicInformation1, BasicInformation2, MainCostInformation1, MainCostInformation2, MainCostDifference, warning_list, Upper1ON, Upper2ON, UpperDP, UpperNC
        , Sole1ON, Sole2ON, SoleDP, SoleNC, SolePaint1ON, SolePaint2ON, SolePaintDP, SolePaintNC, Sundries1ON, Sundries2ON, SundriesDP, SundriesNC, Packing1ON, Packing2ON, PackingDP,  PackingNC, df1, df2])

