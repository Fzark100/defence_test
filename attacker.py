import sys
import os
import random
import numpy as np
import time
class Attacker:#进攻和治疗
    def __init__(self, damage, atk_dur, hits=1):
        self.damage = damage
        self.atk_dur = atk_dur
        self.hits = hits
        self.timer = 0
    def attack(self, Defencer):

        if self.attackable():#检查是否能攻击
            if self.damage>0:#攻击力大于0为伤害，攻击小于0为治疗
                Defencer.attacked(self.damage, self.hits)
                self.timer = self.atk_dur#攻击进入冷却
                return Defencer.retire()#返回结果
            elif not Defencer.healthy():#检查是否健康（满血）
                Defencer.healed(-self.damage)
                self.timer = self.atk_dur
    def cool_dowm(self, time):
        self.timer = self.timer - time
    def attackable(self):
        return self.timer<=0

    # @property
    # def damage(self):
    #     return self.damage

    # @damage.setter
    # def damage(self, damage):
    #     if np.around(damage) == 0:
    #         raise ValueError('damage cannot be 0!')
    #     self.damage = damage

    # @property
    # def atk_dur(self):
    #     return self.atk_dur

    # @atk_dur.setter
    # def atk_dur(self, atk_dur):
    #     if atk_dur<0:
    #         raise ValueError('atk_dur must be larger than 0!')
    #     self.atk_dur = atk_dur

    # @property
    # def hits(self):
    #     return self.hits

    # @hits.setter
    # def hits(self, hits):
    #     if not isinstance(hits, int):
    #         raise ValueError('hits must be an integer!')
    #     if hits<0:
    #         raise ValueError('hits must be larger than 0!')
    #     self.hits = hits


