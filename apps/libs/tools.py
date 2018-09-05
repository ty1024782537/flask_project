import uuid
import datetime


# 产生16位的UUID字符串
def generate_merchant_uuid():
    tre = str(uuid.uuid4())
    tt = str(datetime.date.today())
    oo = ''.join(tre.split('-')[2:4])
    cc = ''.join(tt.split('-')[0:3])
    num = cc + oo
    # print(num)
    return num


# if __name__ == '__main__':
#     generate_merchant_uuid()
