# -*-coding:utf-8 -*-
def shopping_log(goods_dic, customer_no, total_consumer_record):
    '''记录购买行为

    参数：
        goods_dic：字典类型，key为购买的奶茶类型编号，value为购买的数量
        customer_no：用户编号
        total_consumer_record：总体购买记录，列表类型，其中每个元素为一次购买记录。
                               元素为字典类型，字典由三个key-value对组成，分别记录某一个奶茶订单的信息：
                               用户id（customer_no），奶茶编号（milktea_no）,购买数量（milktea_amount）。

    返回值：
        总体购买记录列表。

    '''
    for milktea_no, milktea_amount in goods_dic.items():
        single_consumer_record = {}
        single_consumer_record['customer_no'] = customer_no
        single_consumer_record['milktea_no'] = milktea_no
        single_consumer_record['milktea_amount'] = milktea_amount

        # TODO
        # 将single_sonsumer_record项添加到total_consumer_record中
        # 补全代码
        total_consumer_record.append(single_consumer_record)
    return total_consumer_record
