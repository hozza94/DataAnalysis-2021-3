import json, pymysql

with open('06.MySQL\mysql.json', 'r') as file:
  config_str = file.read()
config = json.loads(config_str)

conn = pymysql.connect(**config) # dictionary unpacking

print(conn)


# 1. 월별 매출 이익
# 2. 거래처별 매출 이익
# 3. 거래처별 판매제품 및 수량
# 4. 제품별 판매수량 매출 이익
# 5. 카테고리별 매출 이익 표 및 그래프


# month값을 가지고 월별 매출 이익을 return 하는 함수
def monthly_profit(config):
    conn = pymysql.connect(**config) # dictionary unpacking
    cur = conn.cursor()

    sql = '''
        SELECT uid, uname, email
        FROM product
        WHERE is_deleted = 0 ORDER BY reg_date;
    '''

    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def company_profit(company):
    pass

def company_count(company):
    pass

def product_profit(product):
    pass

def category_profit(category):
    pass
