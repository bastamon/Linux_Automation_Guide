# -*-coding:utf-8 -*-
total_consumer_record = []
# vip会员记录
vip_dic = {}

i = 1
while True:
    print('\n欢迎光临火星奶茶馆！本店售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！\n 1）原味冰奶茶 13元  2）香蕉冰奶茶 15元 '
          ' 3) 草莓冰奶茶 15元  4）蒟蒻冰奶茶 17元  5）珍珠冰奶茶 17元')
    print('本店每日接待5位顾客，您是今天第{}位幸运儿'.format(i))

    # 调用shopping_produre进行商品选择
    goods_dic = shopping_procedure()
    # TODO
    # 若此次没有做商品选择，跳过后续计算费用环节继续下个循环
    # 补全代码
    continue
    # 调用receipt_print计算费用总额
    vip_no = input('请输入您的专属会员号(新会员直接设置会员号即可，激活手机号方可享受会员价）：')
    total_money = receipt_print(goods_dic)

    # TODO
    # 如果vip_no在vip_dic中能够查到，将总价打9折，并显示'您可以享受会员价，折后总价：xx元'，其中xx为计算得到的折后价格。
    # 否则，打印'请输入您的手机号激活会员：'提示用户输入电话号码。将非会员添加到会员表vip_dic中，
    # 新添项的key是vip_no，value是用户输入的电话号码。
    # 补全代码
    if vip_no in vip_dic:
        total_money *= 0.9
        print('您可以享受会员价，折后总价：{}元'.format(total_money))
    else:
        vip_dic[vip_no] = input('请输入您的手机号激活会员：')
    # 调用shopping_log记录用户购买动作
    total_consumer_record = shopping_log(goods_dic, vip_no, total_consumer_record)

    print("\n********************************************************")
    print('\t火星奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t    祝您今日购物愉快！诚挚欢迎您再次光临！')
    print("********************************************************")

    # TODO
    # 当购买次数大于等于5次时，打印'今日已闭店，欢迎您明天光临！'并退出购买循环
    # 补全代码
    if i < 5:
        i += 1
    else:
        print('今日已闭店，欢迎您明天光临！')
        break
# 打印今天的所有销售情况
print('今日售卖情况:{}'.format(total_consumer_record))
