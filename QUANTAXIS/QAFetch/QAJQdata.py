# coding:utf-8
from jqdatasdk import bank_indicator, security_indicator, insurance_indicator, indicator

from QUANTAXIS.QAUtil import QASETTING

try:
    import jqdatasdk
    # jqdatasdk.auth(input('account:'),input('password:'))
    username,password=QASETTING.get_jq_auth()
    jqdatasdk.auth(username, password)
except:
    raise ModuleNotFoundError


def get_price(code="600000.XSHG"):
    return jqdatasdk.get_price(code,end_date='2018-05-14')

def QA_fetch_get_finance_indicator(code="600000.XSHG",date=None,statDate=None):
    '''
    得到财务指标，https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%8C%87%E6%A0%87%E6%95%B0%E6%8D%AE
    :param code:
    :param date:
    :param statDate:
    :return:
    '''
    q = jqdatasdk.query(
        indicator
        ).filter(
        indicator.code == code
        )
    return jqdatasdk.get_fundamentals(q,date=date,statDate=statDate)


def QA_fetch_get_valuation(code_list=["600000.XSHG"],date=None):
    '''
    https://www.joinquant.com/help/api/help?name=Stock#%E5%B8%82%E5%80%BC%E6%95%B0%E6%8D%AE
    :param code:
    :param date:
    :return:
    '''
    q = jqdatasdk.query(
        jqdatasdk.valuation
        ).filter(
        jqdatasdk.valuation.code.in_(code_list)
        )
    return jqdatasdk.get_fundamentals(q,date=date)

def QA_fetch_get_finance_bank_indicator(code="600000.XSHG",date=None,statDate=None):
    '''
    得到银行的专项指标，https://www.joinquant.com/help/api/help?name=Stock#%E9%93%B6%E8%A1%8C%E4%B8%9A%E4%B8%93%E9%A1%B9%E6%8C%87%E6%A0%87
    :param code:
    :param date:
    :param statDate:
    :return:
    '''
    q = jqdatasdk.query(
        bank_indicator
        ).filter(
            bank_indicator.code == code
        )
    return jqdatasdk.get_fundamentals(q,date=date,statDate=statDate)


def QA_fetch_get_finance_security_indicator(code="600000.XSHG",date=None,statDate=None):
    '''
    得到券商的专项指标，说明https://www.joinquant.com/help/api/help?name=Stock#%E5%88%B8%E5%95%86%E4%B8%9A%E4%B8%93%E9%A1%B9%E6%8C%87%E6%A0%87
    :param code:
    :param date:
    :param statDate:
    :return:
    '''
    q = jqdatasdk.query(
        security_indicator
        ).filter(
        security_indicator.code == code
        )
    return jqdatasdk.get_fundamentals(q,date=date,statDate=statDate)

def QA_fetch_get_insurance_security_indicator(code="600000.XSHG",date=None,statDate=None):
    '''
    得到保险的专项指标，说明https://www.joinquant.com/help/api/help?name=Stock#%E4%BF%9D%E9%99%A9%E4%B8%9A%E4%B8%93%E9%A1%B9%E6%8C%87%E6%A0%87
    :param code:
    :param date:
    :param statDate:
    :return:
    '''
    q = jqdatasdk.query(
        insurance_indicator
        ).filter(
        insurance_indicator.code == code
        )
    return jqdatasdk.get_fundamentals(q,date=date,statDate=statDate)

def QA_fetch_get_stock_industry(security, date=None):
    '''
    得到股票的行业，todo:待完成
    :param security:
    :param date:
    :return:
    '''
    return jqdatasdk.get_industry(security, date)

def QA_fetch_industry_stocks(industry_code, date=None):
    '''
    得到行业的成分股 todo:
    :param industry_code:
    :param date:
    :return:
    '''
    return jqdatasdk.get_industry_stocks(industry_code, date)


def QA_fetch_holder_num(code, date,limit=100):
    '''
    获取上市公司全部股东户数，A股股东、B股股东、H股股东的持股户数
    :param industry_code:
    :param date:
    :return:
    '''
    finance=jqdatasdk.finance
    q = jqdatasdk.query(finance.STK_HOLDER_NUM).filter(finance.STK_HOLDER_NUM.code == code,
                                             finance.STK_HOLDER_NUM.pub_date >=date).limit(limit)
    return finance.run_query(q)




if __name__ =='__main__':
    print(get_price())
"""

get_price

可查询股票、基金、指数、期货的历史及当前交易日的行情数据

可指定单位时间长度，如一天、一分钟、五分钟等

可查询开盘价、收盘价、最高价、最低价、成交量、成交额、涨停、跌停、均价、前收价、是否停牌

支持不同的复权方式

​

get_trade_days

查询指定时间范围的交易日

​

get_all_trade_days

查询所有的交易日

​

get_extras

查询股票是否是ST

查询基金的累计净值、单位净值

查询期货的结算价、持仓量

​

get_index_stocks

查询指定指数在指定交易日的成分股

​

get_industry_stocks

查询指定行业在指定交易日的成分股

​

get_industries

查询行业列表

​

get_concept_stocks

查询指定概念在指定交易日的成分股

​

get_concepts

查询概念列表

​

get_all_securities

查询股票、基金、指数、期货列表

​

get_security_info

查询单个标的的信息

​

get_money_flow

查询某只股票的资金流向数据

​

get_fundamentals

查询财务数据，包含估值表、利润表、现金流量表、资产负债表、银行专项指标、证券专项指标、保险专项指标

​

get_fundamentals_continuously

查询多日的财务数据

​

get_mtss

查询股票、基金的融资融券数据

​

get_billbord_list

查询股票龙虎榜数据

​

get_locked_shares

查询股票限售解禁股数据

​

get_margincash_stocks

获取融资标的列表


get_marginsec_stocks

获取融券标的列表

​

get_future_contracts

查询期货可交易合约列表

​

get_dominant_future

查询主力合约对应的标的

​

get_ticks

查询股票、期货的tick数据

​

normalize_code

归一化证券编码

​

macro.run_query

查询宏观经济数据，具体数据见官网API https://www.joinquant.com/data/dict/macroData

​

alpha101

查询WorldQuant 101 Alphas 因子数据，具体因子解释见官网API https://www.joinquant.com/data/dict/alpha101

​

alpha191

查询短周期价量特征 191 Alphas 因子数据，具体因子解释见官网API https://www.joinquant.com/data/dict/alpha191

​

technical_analysis

技术分析指标，具体因子解释见官网API https://www.joinquant.com/data/dict/technicalanalysis

​

​

baidu_factor

查询股票某日百度搜索量数据
"""