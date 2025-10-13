[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/peCxHnxY)
# EE267_LAB0: Access Carla

Please refer to the instructions [here](https://docs.google.com/document/d/1PwzTUXI43FQObJ2Cy7xu3a_J-AEyEal76FWF_SttEhE/edit?usp=sharing)

## Part 01
- Go to the Carla root directory: `cd ~/carla`
- Run `./CarlaUE4.sh` for interactive environment and `./CarlaUE4.sh -RenderOffScreen` for background simulation (Useful when control is exclusively through API).

## Part 02
- We created the environment called `trojan` with Python version 3.9
- Access this environment with `conda activate trojan` or use the prebuilt environment with `conda activate carla`
- `cd ~/carla/ee267-fall25-lab0-trojanhorsepower`
- `vglrun python manual_control.py` - For manual control
- `vglrun python automatic_control.py` - For automatic control

## Part 03
- Start the simulator following the steps in Part 01 (interactive sim) and activate the conda environment like in Part 02
- Navigate to anywhere you like in the simulator.
- `cd ~/carla/ee267-fall25-lab0-trojanhorsepower && python traffic_manager.py`
- Run code cells step by step in the notebook `traffic_manager.ipynb` if needed.


## Part 04
- Start the simulator following the steps in Part 01 (background sim) and activate the conda environment like in Part 02
- run all code cells of `bounding_boxes.ipynb` to achieve all the similar results.
- Find the PASCAL VOC output at `./output/part_04/`

## Part 05
- Start the simulator following the steps in Part 01 (interactive sim) and activate the conda environment like in Part 02
- `cd ~/carla/ee267-fall25-lab0-trojanhorsepower && python instance_segmentation.py`
- Run code cells step by step in the notebook `instance_segmentation.ipynb` if needed.
- Find the image output at `./output/part_05/instance_segmentation.png`