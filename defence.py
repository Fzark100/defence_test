from defencer import Croissant, Hoshiguma, Nian
from attacker import Attacker
import numpy as np
import matplotlib.pyplot as plt

def defence_test1(defencer, attacker, healer, t_max = 30, test_times=1, delta_time = 0.05, verbose=False):
    time_accum = []
    times = test_times
    t_delta = delta_time
    for i in range(times):
        t = 0
        if verbose: print('*' * 20, '第', i + 1, '次尝试', '*' * 20)
        while t < t_max:
            attacker.cool_dowm(t_delta)
            healer.cool_dowm(t_delta)
            attacker.attack(defencer)
            if defencer.retire():
                break
            healer.attack(defencer)
            t += t_delta
        time_accum.append(np.around(t))
        defencer.redeploy()

        if verbose: print('这一轮坚持了：%d秒' % t)
    return time_accum

if __name__ == '__main__':
    verbose = False #是否显示战斗日志，当大规模测试时建议设置成False
    Croissant = Croissant(HP=3670, DEF=796*1.7, miss=23*2, verbose=verbose)
    enemy1 = Attacker('斧头', 3780, 3.5)
    healer1 = Attacker("满潜赫默7级一技能", -581*1.7, 2.85/1.14)
    times = 10000
    skill_dur = 30
    time_accum = defence_test1(Croissant, enemy1, healer1, t_max=30, test_times=times, verbose=verbose)

    print(sum(time_accum)/times)
    x = range(skill_dur+1)
    y = []
    for num in x:
        y.append(time_accum.count(num))
    print(x)
    print(y)
    plt.bar(x, y)
    plt.show()

