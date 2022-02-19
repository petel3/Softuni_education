n=int(input())
hero={}
max_hp=100
max_mp=200
for _ in range(n):
    hero_name,hitpoints,mana=input().split()
    hitpoints=int(hitpoints)
    mana=int(mana)
    hero[hero_name]={'HP':hitpoints,'MP':mana}
commands=input()
while commands !="End":
    task=commands.split(" - ")
    if task[0]=="CastSpell":
        hero_name=task[1]
        mp_need=int(task[2])
        spell_name=task[3]
        if hero[hero_name]['MP']>=mp_need:
            hero[hero_name]['MP']-=mp_need
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif task[0]=="TakeDamage":
        hero_name=task[1]
        damage=int(task[2])
        attacker=task[3]
        if hero[hero_name]['HP']-damage>0:
            hero[hero_name]['HP'] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero[hero_name]['HP']} HP left!")
        else:
            del hero[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif task[0]=="Recharge":
        hero_name=task[1]
        mp_recover=int(task[2])
        if hero[hero_name]['MP'] +mp_recover<=max_mp:
            hero[hero_name]['MP']+=mp_recover
            print(f"{hero_name} recharged for {mp_recover} MP!")
        else:
            recovered = max_mp - hero[hero_name]['MP']
            hero[hero_name]['MP']=max_mp
            print(f"{hero_name} recharged for {recovered} MP!")
    elif task[0]=="Heal":
        hero_name = task[1]
        hp_recover = int(task[2])
        if hero[hero_name]['HP'] + hp_recover <= max_hp:
            hero[hero_name]['HP'] += hp_recover
            print(f"{hero_name} healed for {hp_recover} HP!")
        else:
            healed = max_hp - hero[hero_name]['HP']
            hero[hero_name]['HP'] = max_hp
            print(f"{hero_name} healed for {healed} HP!")

    commands=input()
for hero,parameters in sorted(hero.items(), key=lambda tkvp: (-tkvp[1]['HP'],tkvp[0])):
    print(f"{hero}")
    print(f"HP: {parameters['HP']}")
    print(f"MP: {parameters['MP']}")