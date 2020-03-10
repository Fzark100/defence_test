import sys
import os
import random
import numpy as np
import time
class Defencer:
    def __init__(self, HP, DEF, evd=0):
        #hp血量, DEF防御,evd闪避
        self.hp = HP
        self.HP_rest = HP
        self.defence = DEF
        self.evd = evd

    def set_attacker(self, damage, attack_dur, hits=1):
        #damage攻击力，attack_dur攻击间隔
        self.damage = damage
        self.attack_dur = attack_dur
        self.hits = hits
    def set_healer(self, recovery, heal_dur=2.85):
        #recovery回复量， heal_dur回复间隔
        self.recovery = recovery
        self.heal_dur = heal_dur

    def reburn(self):
        self.HP_rest=self.hp

    def valid_judge(self):
        return random.randint(0,99)>=self.evd
    def retire(self):
        return self.HP_rest<=0
    def attack(self, t):
        assert self.damage
        if self.valid_judge() and t - np.floor(t/self.attack_dur)*self.attack_dur<0.05:
            self.HP_rest = self.HP_rest - max(self.damage-self.defence, self.damage*0.05)*self.hits
    def heal(self, t):
        assert self.recovery
        if t - np.floor(t/self.heal_dur)*self.heal_dur<0.05:
            self.HP_rest = min(self.HP_rest+self.recovery, self.hp)

if __name__ == '__main__':
    Croissant = Defencer(3670, 1353, 46)
    Croissant.set_attacker(3700, 3.5)
    Croissant.set_healer(620*1.8, 2.85/1.2)
    time_accum = 0
    times = 1000
    for i in range(times):
        t = 0
        while (not Croissant.retire()) and t < 30:
            Croissant.attack(t)
            Croissant.heal(t)
            t += 0.05
        time_accum +=t
        Croissant.reburn()

    print(time_accum/times)

