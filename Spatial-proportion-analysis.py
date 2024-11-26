df = pd.read_csv(r'D:\Feature.csv')
df_points = np.genfromtxt(r'D:\Feature.csv', delimiter=',', usecols=(3, 2), skip_header=1)  # usecols用于获取经纬度，使用语法为usecols=(经度, 纬度)
# 可以对csv数据进行筛选(数据预处理)，在本例中我将从stages和renovation两个字段进行数据筛选，筛选字段根据需求选择即可，无需筛选可在后续代码中使用None即可
if stages is None:
def csv_list(stages, renovation):
        if renovation is None:
            list_of_analysis = df
        else:
            list_of_analysis = df[df['label'] == renovation]
    elif renovation is None:
        list_of_analysis = df[df['stages'] == stages]
    else:
        list_of_analysis = df[df['stages'] == stages]
        list_of_analysis = list_of_analysis[list_of_analysis['label'] == renovation]
    return list_of_analysis

def tree_Points(tree_stages, tree_renovation, analysis_stages, analysis_renovation, analysis_radius):
    """
    tree_Points是为了解决“x点群在y点群中的更新比例与未更新比例情况如何”的问题(),
    tree_stages与tree_renovation为KDTree数据的选定参数(即筛选y点群),
    analysis_stages、analysis_renovation与analysis_radius为tree.query_ball_point函数的选定参数(即筛选点群)
    """
    csv_list(tree_stages, tree_renovation).to_csv(r'D:\tree_csvfile.csv', index=None)
    tree_points = np.genfromtxt(r'D:\tree_csvfile.csv', delimiter=',', usecols=(3, 2), skip_header=1)
    tree_df = pd.read_csv(r'D:\tree_csvfile.csv')
    csv_list(analysis_stages, analysis_renovation).to_csv(r'D:\analysis_csvfile.csv', index=None)
    analysis_points = np.genfromtxt(r'D:\analysis_csvfile.csv', delimiter=',', usecols=(3, 2), skip_header=1)
    analysis_df = pd.read_csv(r'D:\analysis_csvfile.csv')
    tree = spatial.cKDTree(tree_points)
    FieldPoints = tree.query_ball_point(analysis_points,  analysis_radius)  # 输出一个1行n列的列表，每列内容为分析点的邻近点id
    num_Points = len(FieldPoints)  # 统计分析点个数
    rate_False_all = 0
    rate_Renovation_all = 0
    fid = 0
    rateRenovationList = []
    for a in FieldPoints:
        df_id = analysis_df.loc[fid, 'ID']
        tree_index = str(tree_df.loc[tree_df['ID'] == df_id].index)
        a.remove(int(tree_index[12:-17]))  # 舍去分析点本身
        print('分析点id=', analysis_df.loc[fid, 'ID'], sep='')
        num = len(a)  # 某分析点邻域点个数
        num_FalsePoints = 0  # 未更新点个数
        num_RenovationPoints = 0  # 更新点个数
        for b in a: 
            n = tree_df.loc[b, 'label']  # 指定字段进行计算，在本例中，label共有两种情况，分别为1或-1
            if n == -1:  # 注意未更新的标签是0还是-1
                num_FalsePoints += 1
            else:
                num_RenovationPoints += 1
        if num != 0:
            rate_False_all += num_FalsePoints / num
            rate_Renovation_all += num_RenovationPoints / num
            print('未更新比例=', '%.5f' % (num_FalsePoints/num), sep='')
            print('更新比例=', '%.5f' % (num_RenovationPoints/num), sep='')
            rateRenovationList.append(num_RenovationPoints/num)
            print('-' * 15)
        else:
            num_Points -= 1
            print(str(analysis_radius) + '米内没有相邻点')
            rateRenovationList.append(0)
            print('-' * 15)
        fid += 1
    print('分析半径为', analysis_radius)
    if num_Points != 0:
        print('平均未更新比例=', '%.5f' % (rate_False_all / num_Points), sep='')
        print('平均更新比例=', '%.5f' % (rate_Renovation_all / num_Points), sep='')
    else:
        print('平均未更新比例=0')  # 此时意味着在指定半径内，所有分析点均没有邻域点
        print('平均更新比例=0')  # 此时意味着在指定半径内，所有分析点均没有邻域点
    analysis_df['rateRenovation_' + str(analysis_radius)] = rateRenovationList
    analysis_df.to_csv(r'D:\feature.csv', index = None)
# 开始分析
tree_Points('AB', None, 'AB', None, 500)  # 仅计算在AB时期的样本点，在半径500米范围内的城市更新比例