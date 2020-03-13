import sys
import os
import random
import numpy as np
import time
class Defencer:
    def __init__(self, name, HP, DEF, miss=0, verbose=False):
        #hp血量, DEF防御,miss闪避为0到99的整数
        self.name = name
        self.hp = HP
        self.defence = DEF
        self.miss = miss
        self.HP_rest = self.hp

        self.verbose = verbose#是否显示战斗日志

    def redeploy(self):#再部署
        self.HP_rest=self.hp
    def retire(self):#血量耗尽
        rvl = self.HP_rest<=0
        if rvl and self.verbose:
            print(self.name, "倒下了！")
        return rvl
    # def health(self):
    #     return self.HP_rest
    def healthy(self):#判断是否满血
        return self.HP_rest == self.hp

    def valid_judge(self, enemy):#判断是否闪避
        rvl = random.randint(0,99)>=self.miss
        if self.verbose:
            if rvl:
                print(enemy, '对', self.name, '发动攻击,', "成功命中！")
            else:
                print(enemy, '对', self.name, '发动攻击,', self.name, "闪避了这次攻击！")
        return rvl
    def attacked(self, enemy, damage, hits):
        if self.valid_judge(enemy):
            self.HP_rest = self.HP_rest - max(damage-self.defence, damage*0.05)*hits
            if self.verbose:
                print(enemy, '对', self.name, "造成了", np.around(max(damage-self.defence, damage*0.05)*hits), '点伤害,',
                  self.name, '还剩下', np.around(max(self.HP_rest, 0)), '血。')
    def healed(self, friends, recovery):
        if self.verbose:
            print(friends, '恢复了', self.name, np.around(min(recovery, self.hp - self.HP_rest)), '点生命值,', self.name, '还剩',
              np.around(min(self.HP_rest+recovery, self.hp)), '血')
        self.HP_rest = min(self.HP_rest+recovery, self.hp)

class Croissant(Defencer):
    def __init__(self, name='可颂', HP=3670, DEF=770, miss=20, verbose=False):  # 用的都是一潜满级数值
        super().__init__(name, HP, DEF, miss, verbose)


class Hoshiguma(Defencer):
    def __init__(self, name= '星熊', HP=3850, DEF=783, miss=25, verbose=False):
        super().__init__(name, HP, DEF, miss, verbose)


class Nian(Defencer):
    def __init__(self, name='年', HP=4099, DEF=796, miss=0, verbose=False):
        super().__init__(name, HP, DEF, miss, verbose)

