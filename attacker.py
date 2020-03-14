import sys
import os
import random
import numpy as np
import time
class Attacker:#进攻和治疗
    def __init__(self, name='Null', damage=100, atk_dur=1, hits=1):
        self.name = name
        self.damage = damage
        self.atk_dur = atk_dur
        self.hits = hits
        self.timer = 0
    def attack(self, Defencer):

        if self.attackable():#检查是否能攻击
            if self.damage>0:#攻击力大于0为伤害，攻击小于0为治疗
                Defencer.attacked(self.name, self.damage, self.hits)
                self.timer = self.atk_dur#攻击进入冷却
                return Defencer.retire()#返回结果
            elif not Defencer.healthy():#检查是否健康（满血）
                Defencer.healed(self.name, -self.damage)
                self.timer = self.atk_dur
    def cool_dowm(self, time):
        self.timer = self.timer - time
    def attackable(self):
        return self.timer<=0
    def refresh(self):#重置攻击
        self.timer = self.atk_dur
