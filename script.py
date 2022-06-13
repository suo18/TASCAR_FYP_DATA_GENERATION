import os
from random import randrange
import random

# function to add "" in our strings for tascar

def strToStr(blockname):

    return '"' + blockname + '"'


# define absolute path to avoid repetition
path_absolute = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/TASCAR_SIMULATIONS_01/"

for i in range(10): 
    # generate coordinates of the receiver
    x_receiver = random.uniform(0, 1)
    y_receiver = random.uniform(0, 1)
    z_receiver = random.uniform(0, 1)

    # generate coordinates of the source
    x_source = random.uniform(0, 1)
    y_source = random.uniform(0, 1)
    z_source = random.uniform(0, 1)


    ### SOURCE
    t = 0

    x = 0

    y = 0.6

    z = 0.6

    file_source = path_absolute + "sources_template.tsc"

    # Open current tsc file and read it to save it as a string

    fin = open(file_source)

    temp_receiver = fin.read()

    fin.close()

    # replace parameters in {} with whatever string you want

    source = temp_receiver.format(t = t,

    x = x,

    y = y,

    z = z,

    ) 


    ### RECEIVER

    # is id path necessary ? 
    id = 2

    # receiver parameters - add the paths for the receiver, source csv files 

    receiver_pos =  f'/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/position_scene1.csv'

    receiver_ori =  f'/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/orientation_scene1.csv'

    receiver_name = 'hrtf'

    file_receiver = path_absolute + 'receiver_session.tsc'

    # Open current tsc file and read it to save it as a string

    fin = open(file_receiver)

    temp_receiver = fin.read()

    fin.close()

    # replace parameters in {} with whatever string you want

    receiver = temp_receiver.format(receiver_name = strToStr(receiver_name),

    receiver_pos = strToStr(receiver_pos),

    receiver_ori = strToStr(receiver_ori)

    )

    ### SCENE

    file_scene = path_absolute + f'scene_template.tsc'


    fin = open(file_scene)

    temp_scene = fin.read()

    fin.close()

    scene = temp_scene.format(source = source,

    receiver = receiver

    )


    ### CREATE TASCAR SCENE FILE

    file_output = path_absolute + f'scene_1' + '.tsc'

    # file_output = path_scenes + f'SPEAR_n{len(ID_all)}_' + ''.join(sorted(options)) + '.tsc'

    if os.path.exists(file_output):

        output = open(file_output, 'w')

    else:

        output = open(file_output, 'x')

    output.write(scene)

    output.close()

    ### RUN TASCAR

    audio_file = '/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/OUTPUTS/' + f'scene_1' + '.wav'

    # # Run, play and save real time, need to have qjack running

    # os.system("tascar_cli -o " + audio_file + ' ' + file_output)

    # Do not play the scene, just save it

    scene_name = ''

    # os.system(f"tascar_renderfile --scene {scene_name} -o {audio_file} {file_output}")

    os.system(f"tascar_renderfile -o {audio_file} {file_output}")