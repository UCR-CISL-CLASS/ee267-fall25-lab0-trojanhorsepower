# %%
import carla
import random

# %%
# Initialize traffic manager
client = carla.Client('localhost', 2000)
world = client.get_world()

settings = world.get_settings()
settings.synchronous_mode = True
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

traffic_manager = client.get_trafficmanager()
traffic_manager.set_synchronous_mode(True)
traffic_manager.set_random_device_seed(0)
random.seed(0)

# %%
spawn_points = world.get_map().get_spawn_points()

# %%
# Select some models from the blueprint library
models = ['dodge', 'audi', 'model3', 'mini', 'mustang', 'lincoln', 'prius', 'nissan', 'crown', 'impala']
blueprints = []
for vehicle in world.get_blueprint_library().filter('*vehicle*'):
    if any(model in vehicle.id for model in models):
        blueprints.append(vehicle)

# Set a max number of vehicles and prepare a list for those we spawn
max_vehicles = 50
max_vehicles = min([max_vehicles, len(spawn_points)])
vehicles = []

# Take a random sample of the spawn points and spawn some vehicles
for i, spawn_point in enumerate(random.sample(spawn_points, max_vehicles)):
    temp = world.try_spawn_actor(random.choice(blueprints), spawn_point)
    if temp is not None:
        vehicles.append(temp)


# %%
for _ in range(50):
    blueprint = random.choice(world.get_blueprint_library().filter('walker.pedestrian.*'))
    sp = random.choice(spawn_points) if spawn_points else carla.Transform()
    world.try_spawn_actor(blueprint, sp)

# %%
for vehicle in vehicles:
    vehicle.set_autopilot(True)
    traffic_manager.ignore_lights_percentage(vehicle, random.randint(0, 50))

# %%
while True:
    world.tick()


