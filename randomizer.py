import random as ran

with open('abs.txt') as f:
    ab_exercises = f.readlines()
with open('bicep.txt') as f:
    bi_exercises = f.readlines()
with open('leg.txt') as f:
    leg_exercises = f.readlines()
with open('tricep.txt') as f:
    tri_exercises = f.readlines()

workout1 = []
workout2 = []
workout1.append(ab_exercises.pop(ran.randrange(len(ab_exercises))))
workout1.append(bi_exercises.pop(ran.randrange(len(bi_exercises))))
workout1.append(leg_exercises.pop(ran.randrange(len(leg_exercises))))
workout1.append(tri_exercises.pop(ran.randrange(len(tri_exercises))))

workout2.append(ab_exercises.pop(ran.randrange(len(ab_exercises))))
workout2.append(bi_exercises.pop(ran.randrange(len(bi_exercises))))
workout2.append(leg_exercises.pop(ran.randrange(len(leg_exercises))))
workout2.append(tri_exercises.pop(ran.randrange(len(tri_exercises))))

print workout1
print workout2
