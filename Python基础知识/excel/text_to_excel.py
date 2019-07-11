# -*- coding: utf-8 -*-
# coding: utf-8
# @Date:   2019-04-04 22:46:19
# @Last Modified by:   Marte
# @Last Modified time: 2019-04-06 23:33:57
import xlwt
import time
from concurrent.futures import ThreadPoolExecutor

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('tmmr', cell_overwrite_ok=True)


row0 = [u"用户名称", u"流水号", u"提现金额", u"区域", u"提现时间", u"实付金额", u"提现状态", u'银行账户名', u'银行账号', u'开户银行', u'支行名称', u'银行地址',
        u'提现渠道', u'审阅']

for i in range(0, len(row0)):
    sheet1.write(0, i, row0[i])


def clean(data, index):
    print('运行到第' + str(index) + '行')
    sheet1.write(index, 0, str(data[0]))  # 用户名称
    sheet1.write(index, 1, str(data[1]))  # 用户GW号
    sheet1.write(index, 2, str(data[2]))  # 流水号
    sheet1.write(index, 3, str(data[3]) + str(data[4]))  # 提现金额
    sheet1.write(index, 4, str(data[5]))  # 区域
    sheet1.write(index, 5, str(data[6]) + str(data[7]))  # 提现时间
    sheet1.write(index, 6, str(data[8]) + str(data[9]))  # 实付金额
    sheet1.write(index, 7, str(data[10]))  # 提现状态
    sheet1.write(index, 8, str(data[11]))  # 银行账户名
    sheet1.write(index, 9, str(data[12]))  # 银行账号
    sheet1.write(index, 10, str(data[13]))  # 开户银行
    sheet1.write(index, 11, str(data[14]))  # 支行名称
    sheet1.write(index, 12, str(data[15]) + str(data[16]) + str(data[17]))  # 银行地址
    sheet1.write(index, 13, str(data[18]))  # 流水号
    sheet1.write(index, 14, str(data[19]))  # 流水号
    workbook.save('Clean.xls')


if __name__ == '__main__':
    start = time.time()

    file_name = input('Input Target Txt:')
    cpu_s = int(input('Set Threads:'))
    all_infos = [x.strip('\n').split(' ') for x in open(file_name, 'r', encoding='utf-8').readlines()][1:]
    print('转换总行数:{}'.format(len(all_infos)))
    with ThreadPoolExecutor(cpu_s) as p:
        for index, data in enumerate(all_infos):
            p.submit(clean, data, index + 1)

    print("[完成]已导出:Clean.xls")
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
