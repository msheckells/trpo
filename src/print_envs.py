from gym import envs
from gym_mobot.envs import CarModelEnv
envids = [spec.id for spec in envs.registry.all()]
for envid in sorted(envids):
    print(envid)
