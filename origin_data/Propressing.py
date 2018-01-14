import pandas as pd
import datetime
import os

data_map = pd.read_csv('/Users/pansmac/Desktop/data_map.csv', encoding='gb2312')
data_read = pd.read_csv('/Users/pansmac/Desktop/kgl-topsy20171215.txt',
                        dtype={u'VAL': str}, parse_dates=[u'RCVD_DT_TM'],
                        date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
data = pd.merge(data_read, data_map, left_on=['DETCTOR_DEVICE_ID'], right_on=['DEVICE_ID'])  # map wire no
data = data.set_index('WIRE_NO')  # set index
data = data[[u'VAL', u'RCVD_DT_TM']]
data.loc[:, u'RCVD_DT_TM'] = data.loc[:, u'RCVD_DT_TM'] .apply(lambda x: x.time())
bins = [datetime.time(10, 0, 0), datetime.time(10, 15, 0), datetime.time(10, 30, 0), datetime.time(10, 45, 0),
        datetime.time(11, 0, 0)]
os.mkdir(r'save_data')
os.mkdir(r'save_data/switch')
for index in data.index.unique():
    data_index = data.ix[index]
    for ix in range(len(bins)-1):
        data_save = data_index[data_index.RCVD_DT_TM.between(bins[ix], bins[ix+1])]

        file_name = 'save_data/switch/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()

        data_save.to_csv(file_name)

# ----------------------------------AL_DET_INFO_1M
data_read = pd.read_csv('/Users/pansmac/Desktop/AL_DATA/AL_det_info_1m.txt', parse_dates=[u'RCVD_DT_TM'],
                        date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
data = pd.merge(data_read, data_map, left_on=['DETCTOR_DEVICE_ID'], right_on=['DEVICE_ID'])  # map wire no
data = data.set_index('WIRE_NO')  # set index
data = data[[u'VAL', u'TYPE', u'RCVD_DT_TM']]
data.loc[:, u'RCVD_DT_TM'] = data.loc[:, u'RCVD_DT_TM'] .apply(lambda x: x.time())
# bins = [datetime.time(10, 0, 0), datetime.time(10, 15, 0), datetime.time(10, 30, 0)
#         , datetime.time(10, 45, 0), datetime.time(11, 0, 0)]
os.mkdir(r'save_data/det_info_1m')
os.mkdir(r'save_data/det_info_1m/1b')
os.mkdir(r'save_data/det_info_1m/1a')
for index in data.index.unique():
    data_index = data.ix[index]
    data_index_1a = data_index[data_index.TYPE == '1A']
    data_index_1b = data_index[data_index.TYPE == '1B']
    for ix in range(len(bins)-1):
        data_save = data_index_1b[data_index_1b.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/det_info_1m/1b/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)

    for ix in range(len(bins)-1):
        data_save = data_index_1a[data_index_1a.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/det_info_1m/1a/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)

# ----------------------------------------AL_FLOW_OCCUP
data_read = pd.read_csv('/Users/pansmac/Desktop/AL_DATA/AL_flow_occup.txt',  dtype={u'TYPE': str},
                        parse_dates=[u'RCVD_DT_TM'],
                        date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
data = pd.merge(data_read, data_map, left_on=['DETCTOR_DEVICE_ID'], right_on=['DEVICE_ID'])  # map wire no
data = data.set_index('WIRE_NO')  # set index
data = data[[u'VAL', u'TYPE', u'RCVD_DT_TM']]
data.loc[:, u'RCVD_DT_TM'] = data.loc[:, u'RCVD_DT_TM'] .apply(lambda x: x.time())
# bins = [datetime.time(10, 0, 0), datetime.time(10, 15, 0), datetime.time(10, 30, 0)
#         , datetime.time(10, 45, 0), datetime.time(11, 0, 0)]
os.mkdir(r'save_data/flow_occup')
os.mkdir(r'save_data/flow_occup/07')
os.mkdir(r'save_data/flow_occup/08')
for index in data.index.unique():
    data_index = data.ix[index]
    data_index_07 = data_index[data_index.TYPE == '07']
    data_index_08 = data_index[data_index.TYPE == '08']
    for ix in range(len(bins)-1):
        data_save = data_index_07[data_index_07.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/flow_occup/07/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)

    for ix in range(len(bins)-1):
        data_save = data_index_08[data_index_08.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/flow_occup/08/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)

# ----------------------------------------AL_JAM

data_read = pd.read_csv('/Users/pansmac/Desktop/AL_DATA/AL_JAM.txt', index_col=['LINE_ID'],
                        parse_dates=[u'RCVD_DT_TM'],
                        date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
data = data_read[[u'VAL', u'RCVD_DT_TM']]
data.loc[:, u'RCVD_DT_TM'] = data.loc[:, u'RCVD_DT_TM'] .apply(lambda x: x.time())
# bins = [datetime.time(10, 0, 0), datetime.time(10, 15, 0), datetime.time(10, 30, 0)
#         , datetime.time(10, 45, 0), datetime.time(11, 0, 0)]
os.mkdir(r'save_data/jam')
for index in data.index.unique():
    data_index = data.ix[index]
    for ix in range(len(bins)-1):
        data_save = data_index[data_index.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/jam/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)


# ----------------------------------------AL_LINE_INFO
data_read = pd.read_csv('/Users/pansmac/Desktop/AL_DATA/AL_line_info.txt', index_col=['LINE_ID'],
                        parse_dates=[u'RCVD_DT_TM'],
                        date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
data = data_read[[u'TYPE', u'VAL', u'SUM_DELAY', u'AVG_DELAY', u'RCVD_DT_TM']]
data.loc[:, u'RCVD_DT_TM'] = data.loc[:, u'RCVD_DT_TM'] .apply(lambda x: x.time())
# bins = [datetime.time(10, 0, 0), datetime.time(10, 15, 0), datetime.time(10, 30, 0)
#         , datetime.time(10, 45, 0), datetime.time(11, 0, 0)]
os.mkdir(r'save_data/line_info')
os.mkdir(r'save_data/line_info/0A')
os.mkdir(r'save_data/line_info/04')
for index in data.index.unique():
    data_index = data.ix[index]
    data_index_0A = data_index[data_index.TYPE == '0A']
    data_index_04 = data_index[data_index.TYPE == '04']
    for ix in range(len(bins)-1):
        data_save = data_index_0A[data_index_0A.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/line_info/0A/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)

    for ix in range(len(bins)-1):
        data_save = data_index_04[data_index_04.RCVD_DT_TM.between(bins[ix], bins[ix+1])]
        file_name = 'save_data/line_info/04/{}-{}~{}'.format(index, bins[ix], bins[ix+1])
        print file_name
        print data_save.head()
        data_save.to_csv(file_name)

