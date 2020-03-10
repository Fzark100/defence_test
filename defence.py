from defencer import Croissant, Hoshiguma, Nian
from attacker import Attacker

if __name__ == '__main__':
    Croissant = Croissant(HP=3670, DEF=796, miss=20, rank=10, five=1)
    enemy1 = Attacker(3780, 3.5)
    # enemy1.damage = 3780
    # enemy1.atk_dur = 3.5
    healer1 = Attacker(-620*1.8, 3.85/1.2)
    time_accum = 0
    times = 1000
    t_delta = 0.05
    for i in range(times):
        t = 0
        t_max = Croissant.skill_on()
        while (not Croissant.retire()) and t < t_max:
            enemy1.cool_dowm(t_delta)
            healer1.cool_dowm(t_delta)
            enemy1.attack(Croissant)
            healer1.attack(Croissant)
            t +=t_delta
        Croissant.skill_off()
        time_accum += t
        print('try ', i, ' times')
        Croissant.redeploy()

    print(time_accum/times)

