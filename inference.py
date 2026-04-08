import os
from env import EmailEnv

print("[START] Running inference")

env = EmailEnv()

for i in range(3):
    obs = env.reset()
    print("[STEP] Observation:", obs)

    # dummy agent (random)
    action = "spam"

    result = env.step(action)
    print("[STEP] Result:", result)

print("[END] Done")