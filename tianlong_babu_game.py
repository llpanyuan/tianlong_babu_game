"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
1.see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
2.fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
# 导入随机数库
import random
from tonglao import TongLao, XuZhu

# 设定角色初始武力值为一范围内随机数值
tonglao_power = random.randint(300, 400)
wyz_power = random.randint(250, 350)
lqs_power = random.randint(350, 450)
dcq_power = random.randint(500, 550)
xuzhu_power = 0


# 定义游戏主函数：恶搞天龙八部游戏！
def egao_game():
    # 童姥及虚竹类实例化
    tonglao = TongLao(1000, tonglao_power)
    xuzhu = XuZhu(1000, xuzhu_power)
    print("欢迎来到”恶搞天龙八部“游戏！")
    # 获取用户使用游戏角色名字与敌人名字信息
    your_name = input("请从（无崖子/李秋水/丁春秋）中选择你想扮演的角色名字：")
    enemy = input("你想选择的对手是（天山童姥/虚竹）：")
    # 判断敌人是天山童姥还是虚竹
    if enemy == "天山童姥":
        # 判断用户使用角色
        if your_name == "无崖子":
            # 打印游戏角色血量、武力值信息
            print("your hp：{}，your power：{}".format(1000, wyz_power))
            print("你与天山童姥不期而遇！")
            tonglao.see_people(your_name)
            print("你（无崖子）：好，是时候展现真正的技术了！")
            tonglao.fight(1000, wyz_power)
        elif your_name == "李秋水":
            # 打印游戏角色血量、武力值信息
            print("your hp：{}，your power：{}".format(1000, lqs_power))
            print("你被天山童姥逮到了！")
            tonglao.see_people(your_name)
            print("你（李秋水）：哼！老娘从来就没怕过谁，我先杀了你！")
            tonglao.fight(1000, lqs_power)
        elif your_name == "丁春秋":
            # 打印游戏角色血量、武力值信息
            print("your hp：{}，your power：{}".format(1000, dcq_power))
            print("你被天山童姥追杀中。。。")
            tonglao.see_people(your_name)
            print("你（丁春秋）：哈哈哈哈，那你也别怪我心狠手辣了！")
            tonglao.fight(1000, dcq_power)
        else:
            print("请从（无崖子/李秋水/丁春秋）中选择一个角色！")
            egao_game()
    elif enemy == "虚竹":
        if your_name == "无崖子":
            # 打印游戏角色血量、武力值信息
            print("your hp：{}，your power：{}".format(1000, wyz_power))
            print("你（无崖子）：虚竹，让我们开一把黑！")
            xuzhu.read()
            print("你（无崖子）：额。。。好吧老弟")
            print("虚竹：罪过罪过。。。。。。。")
            print("恭喜！你不战而胜了")
        elif your_name == "李秋水":
            # 打印游戏角色血量、武力值信息
            print("your hp：{}，your power：{}".format(1000, lqs_power))
            print("你（李秋水）：哟，这不是小虚竹吗，来和姐姐快活啊！")
            xuzhu.read()
            print("你（李秋水）：真没情趣，不懂浪漫，死去吧")
            print("虚竹：罪过罪过。。。。。。。")
            print("虚竹死在了你的石榴裙下。")
        elif your_name == "丁春秋":
            # 打印游戏角色血量、武力值信息
            print("your hp：{}，your power：{}".format(1000, dcq_power))
            print("你（丁春秋）：你就不想帮童姥杀了我吗？")
            xuzhu.read()
            print("你（丁春秋）：哈哈哈哈，有点儿意思，那我就饶你一命。")
            print("虚竹：罪过罪过。。。。。。。")
            print("你放过了虚竹，并扬长而去~")
        else:
            # 异常处理
            print("请从（无崖子/李秋水/丁春秋）中选择一个角色！")
            egao_game()
    else:
        # 异常处理
        print("请从（天山童姥/虚竹）中选择一个对手！")
        egao_game()


egao_game()
