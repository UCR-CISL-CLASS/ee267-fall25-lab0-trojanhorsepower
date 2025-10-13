# %%
import carla
import random
import queue

# %%
client = carla.Client('localhost', 2000)
world = client.get_world()
settings = world.get_settings()
settings.synchronous_mode = True
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

# %% [markdown]
# ### Set up instance segmentation camera

# %%
spawn_points = world.get_map().get_spawn_points()
spectator = world.get_spectator()

cam_location = carla.Location(x=-46, y=152, z=12)
cam_rotation = carla.Rotation(pitch=-21, yaw=-93.4, roll=0)
camera_transform = carla.Transform(location=cam_location, rotation=cam_rotation)
spectator.set_transform(camera_transform)

instance_camera_bp = world.get_blueprint_library().find('sensor.camera.instance_segmentation')
instance_camera = world.try_spawn_actor(instance_camera_bp, camera_transform)

# %% [markdown]
# ### Populate the scene

# %%
vehicle_bp_library = world.get_blueprint_library().filter('*vehicle*')
radius = 80

for sp in spawn_points:
    vec = [sp.location.x - cam_location.x, sp.location.y - cam_location.y]
    if vec[0]*vec[0] + vec[1]*vec[1] < radius*radius:
        world.try_spawn_actor(random.choice(vehicle_bp_library), sp)
world.tick()

# %% [markdown]
# ### Generate the image

# %%
instance_image_queue = queue.Queue()
instance_camera.listen(instance_image_queue.put)
world.tick()
instance_image = instance_image_queue.get()
instance_image.save_to_disk('output/part05/instance_segmentation.png')

# %%



