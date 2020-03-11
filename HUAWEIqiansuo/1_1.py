# -*-coding:utf-8 -*-
# 定义奶茶商品
milktea_dict = {'1': {'name': '原味冰奶茶', 'price': 13},
                '2': {'name': '香蕉冰奶茶', 'price': 15},
                '3': {'name': '草莓冰奶茶', 'price': 15},
                '4': {'name': '蒟蒻冰奶茶', 'price': 17},
                '5': {'name': '珍珠冰奶茶', 'price': 17},
                }


def shopping_procedure():
    '''获取用户的购买需求输入
    
    返回值：
        字典类型goods_dic，key为所购奶茶的编号，value为编号所对应的奶茶的购买数量。
    
    '''

    # 定义返回字典变量
    goods_dic = {}

    while True:
        # 获取用户所要购买的奶茶编号
        milktea_no = input('请输入您要购买的奶茶编号，取消购物请选择Q,完成购物请选择T: ')

        # TODO
        # 如果输入为‘Q’，退出购买流程
        # 补全代码
        if milktea_no.upper() == 'Q':
            goods_dic.clear()
            continue
        # 如果输入为‘T’，完成购买流程
        # 补全代码
        elif milktea_no.upper() == 'T':
            break
        # TODO，修改if语句条件
        # 如果输入的milktea_no编号在有效范围内
        # 补全代码
        elif 1 <= int(milktea_no) <= 5:
            # 提示用户输入购买数量
            milktea_amount = input('请输入您要购买的数量：')
            if not goods_dic.__contains__(milktea_no):
                # TODO
                # 向goods_dic中加入新项，key为milktea_no，value为milktea_amount
                # 补全代码
                goods_dic[milktea_no]=int(milktea_amount)
            else:
                # TODO
                # 根据输入的milktea_no及milktea_amount，将相应的goods_dic项目元素做累加操作
                # 补全代码
                goods_dic[milktea_no] += int(milktea_amount)
        else:
            print('我们只售卖以上五种奶茶哦！请输入正确的奶茶编号！')
            continue
        print('您已完成奶茶选购，还需要继续购买嘛！')

    return goods_dic
