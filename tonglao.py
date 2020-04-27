# 定义天山童姥类
class TongLao:
    # 初始化
    def __init__(self, hp, power):
        # 定义血量、武力值
        self.hp = hp
        self.power = power

    # 定义方法
    def see_people(self, name):
        if name == "无崖子":
            print("天山童姥：师弟!!!!")
            print("天山童姥：我刚学了天山折梅手，让我们来切磋以下吧！")
        elif name == "李秋水":
            print("天山童姥：呸，贱人，看我不宰了你！")
            print("天山童姥使用了天山折梅手，并向你攻击了过来。")
        elif name == "丁春秋":
            print("天山童姥：叛徒！我杀了你")

    # 定义天山折梅手方法
    def fight_zms(self):
        # 武力值提升10倍，生命值减半
        self.power = self.power * 10
        self.hp = self.hp / 2

    # 定义战斗方法
    def fight(self, enemy_hp, enemy_power):
        # 童姥使用天山折梅手（调用天山折梅手方法）
        self.fight_zms()
        # 战斗血量计算方法
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        # 一回合制战斗结果
        if self.hp > enemy_hp:
            print(self.hp)
            print(enemy_hp)
            print("遗憾！你输了")
        elif self.hp == enemy_hp:
            print("平手")
        elif self.hp < enemy_hp:
            print("恭喜！你赢了")


# 定义虚竹类


class XuZhu(TongLao):
    # 定义念经方法
    def read(self):
        print("虚竹：罪过罪过！")
