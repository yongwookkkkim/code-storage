'''
import simpy

def main():
    env=simpy.Environment()
    env.process(traffic_light(env))
    env.run(until=120)
    print("simulation complete")

def traffic_light(env):
    while True:
        print("Light turned green at t="+str(env.now))
        yield env.timeout(30)
        print("Light turned yellow at t="+str(env.now))
        yield env.timeout(5)
        print("Light turned red at t="+str(env.now))
        yield env.timeout(20)

if __name__=='__main__':
    main()
'''

b=[1,2,3,10,11,12]
print(filter(lambda b: b>=10, b))
print(sum(filter(lambda b: b>=10, b)))