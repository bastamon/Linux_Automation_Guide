# -*-coding:utf-8 -*-
def receipt_print(goods_dic):
    '''打印订单详情并计算总金额
    参数：
        goods_dic：字典类型，key为购买的奶茶类型编号，value为购买的数量
    返回值：
        订单总金额。
    '''
    print('点单完成！您的购买详情为：')

    total_money = 0
    money = 0
    for milktea_no, milktea_amount in goods_dic.items():
        print('{}号奶茶:{}杯'.format(milktea_no, milktea_amount))
        # TODO
        # 将购买milktea_amount数量的milktea_no奶茶所需要的金额汇总到total_money变量
        # 补全代码
        total_money += milktea_amount * milktea_dict[milktea_no]['price']
    print('您的总消费额为：{}元'.format(total_money))
    # 返回金额总数
    return total_money
