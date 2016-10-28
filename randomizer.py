import random as ran
import time

with open('abs.txt') as f:
    ab_exercises = f.readlines()
with open('bicep.txt') as f:
    bi_exercises = f.readlines()
with open('leg.txt') as f:
    leg_exercises = f.readlines()
with open('tricep.txt') as f:
    tri_exercises = f.readlines()
with open('chest.txt') as f:
    chest_exercises = f.readlines()
with open('back.txt') as f:
    back_exercises = f.readlines()
with open('shoulder.txt') as f:
    shoulder_exercises = f.readlines()

workout1 = []
workout2 = []
workout3 = []
workout1.append(ab_exercises.pop(ran.randrange(len(ab_exercises))))
workout1.append(bi_exercises.pop(ran.randrange(len(bi_exercises))))
workout1.append(leg_exercises.pop(ran.randrange(len(leg_exercises))))
workout1.append(tri_exercises.pop(ran.randrange(len(tri_exercises))))
workout1.append(chest_exercises.pop(ran.randrange(len(chest_exercises))))
workout1.append(back_exercises.pop(ran.randrange(len(back_exercises))))
workout1.append(shoulder_exercises.pop(ran.randrange(len(shoulder_exercises))))

workout2.append(ab_exercises.pop(ran.randrange(len(ab_exercises))))
workout2.append(bi_exercises.pop(ran.randrange(len(bi_exercises))))
workout2.append(leg_exercises.pop(ran.randrange(len(leg_exercises))))
workout2.append(tri_exercises.pop(ran.randrange(len(tri_exercises))))
workout2.append(chest_exercises.pop(ran.randrange(len(chest_exercises))))
workout2.append(back_exercises.pop(ran.randrange(len(back_exercises))))
workout2.append(shoulder_exercises.pop(ran.randrange(len(shoulder_exercises))))

workout3.append(ab_exercises.pop(ran.randrange(len(ab_exercises))))
workout3.append(bi_exercises.pop(ran.randrange(len(bi_exercises))))
workout3.append(leg_exercises.pop(ran.randrange(len(leg_exercises))))
workout3.append(tri_exercises.pop(ran.randrange(len(tri_exercises))))
workout3.append(chest_exercises.pop(ran.randrange(len(chest_exercises))))
workout3.append(back_exercises.pop(ran.randrange(len(back_exercises))))
workout3.append(shoulder_exercises.pop(ran.randrange(len(shoulder_exercises))))   
    
temp = open('workout.txt', 'w')
temp.write("--Workout #1--\n")
temp.writelines(workout1)
temp.write("\n--Workout #2--\n")
temp.writelines(workout2)
temp.write("\n--Workout #3--\n")
temp.writelines(workout3)
temp.close()
