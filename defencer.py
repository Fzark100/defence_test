import sys
import os
import random
import numpy as np
import time
class Defencer:
    def __init__(self, HP, DEF, miss=0):
        #hp血量, DEF防御,miss闪避为0到99的整数
        self.hp = HP
        self.defence = DEF
        self.miss = miss

        self.HP_rest = self.hp
        self.defence_current = self.defence
        self.miss_current = self.miss

        # self.defence_buff = 0#来自外界的防御和血量buff,暂未实装
        # self.hp_buff = 0

    def redeploy(self):#再部署
        self.HP_rest=self.hp
    def retire(self):#血量耗尽
        return self.HP_rest<=0
    # def health(self):
    #     return self.HP_rest
    def healthy(self):
        return self.HP_rest==self.hp

    def valid_judge(self):#判断是否闪避
        print("Miss!!")
        return random.randint(0,99)>=self.miss_current
    def attacked(self, damage, hits):
        if self.valid_judge():
            self.HP_rest = self.HP_rest - max(damage-self.defence_current, damage*0.05)*hits
            print('deal ', np.around(max(damage-self.defence_current, damage*0.05)*hits),' damage')
            print('have', np.around(max(self.HP_rest, 0)), ' hp rest')
    def healed(self, recovery):
        print('get healing ', np.around(min(recovery, self.hp - self.HP_rest)))
        self.HP_rest = min(self.HP_rest+recovery, self.hp)
        print('have', np.around(max(self.HP_rest, 0)), ' hp rest')
    def defence_refresh(self):
        self.defence_current = self.defence*(1+self.defence_buff)

    @property
    def defence_buff(self):
        return self.defence_buff

    @defence_buff.setter
    def defence_buff(self, defence_buff):
        self.defence_buff = defence_buff

    @property
    def hp_buff(self):
        return self.hp_buff

    @hp_buff.setter
    def hp_buff(self, hp_buff):
        self.hp_buff = hp_buff

class Croissant(Defencer):
    def __init__(self, HP=3670, DEF=796, miss=20, rank=7, five=False):  # rank技能等级
        super().__init__(HP, DEF, miss)
        self.rank = rank-1
        self.defence_scale =float(list([20, 20, 20, 30, 30, 30, 40, 50, 60, 70])[rank-1])*0.01
        self.miss_scale = float(list([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])[rank-1])*0.01
        self.defence_skill = False
        self.miss = self.miss + 0.03*five


    def skill_on(self):
        assert not self.defence_skill
        self.defence_current = self.defence * (1+self.defence_scale)
        self.miss_current = self.miss * (1+self.miss_scale)
        self.defence_skill = True
        return 30  # 技能持续时间

    def skill_off(self):
        assert self.defence_skill
        self.defence_current = self.defence
        self.miss_current = self.miss
        self.defence_skill = False


class Hoshiguma(Defencer):
    def __init__(self, HP=3850, DEF=813, miss=25, rank=7, six=False):#rank技能等级
        super().__init__(HP, DEF, miss)
        self.rank = rank
        self.defence_scale = float(list([60, 65, 70, 80, 85, 90, 100, 110, 120, 130])[rank-1])*0.01
        self.defence_skill = False
        self.defence_scale2 = 0.06 + six*0.02
        self.defence_current = self.defence*(1+self.defence_scale2)
    def skill_on(self):
        assert not self.defence_skill
        self.defence_current = self.defence*(1+self.defence_scale2+self.defence_scale[self.rank])
        self.defence_skill = True
        return 25#技能持续时间
    def skill_off(self):
        assert self.defence_skill
        self.defence_current = self.defence*(1+self.defence_scale2)
        self.defence_skill = False

class Nian(Defencer):
    def __init__(self, HP=4099, DEF=826, miss=0, rank=7, five=False):#rank技能等级
        super().__init__(HP, DEF, miss)
        self.rank = rank
        self.defence_scale = float(list([60, 65, 70, 80, 85, 90, 100, 110, 120, 130])[rank-1])*0.01
        self.defence_skill = False
        self.hp_scale =0.16 + 0.04*five
        self.hp = self.hp*(1+self.hp_scale)
    def skill_on(self):
        assert not self.defence_skill
        self.defence_current = self.defence*(1+self.defence_scale[self.rank])
        self.defence_skill = True
        return 35#技能持续时间
    def skill_off(self):
        assert self.defence_skill
        self.defence_current = self.defence
        self.defence_skill = False