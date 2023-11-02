import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# กำหนดตัวแปร Input
traffic_count = ctrl.Antecedent(np.arange(0, 101, 1), 'Traffic_Count')
traffic_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'Traffic_Speed')

# กำหนดตัวแปร Output
traffic_light_support = ctrl.Consequent(np.arange(0, 101, 1), 'Traffic_Light_Support')

# กำหนดฟังก์ชันการเชื่อมั่น
traffic_count.automf(3)
traffic_speed.automf(3)
traffic_light_support.automf(3)

# กำหนดกฎควบคุม
rule1 = ctrl.Rule(traffic_count['poor'] & traffic_speed['poor'], traffic_light_support['good'])
rule2 = ctrl.Rule(traffic_count['average'] & traffic_speed['average'], traffic_light_support['average'])
rule3 = ctrl.Rule(traffic_count['good'] & traffic_speed['good'], traffic_light_support['poor'])

# สร้างระบบควบคุม
traffic_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
traffic_system = ctrl.ControlSystemSimulation(traffic_ctrl)



traffic_system.input['Traffic_Count'] = 20
traffic_system.input['Traffic_Speed'] = 30

traffic_system.compute()
traffic_sup = round(traffic_system.output['Traffic_Light_Support'],5)

print("Traffic Light Support:", traffic_sup)

traffic_light_support.view(sim=traffic_system, fuzzy_number=101, view='simulation')
plt.show()

