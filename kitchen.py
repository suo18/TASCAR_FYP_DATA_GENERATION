
import os
from random import randrange
from path import Path
from random import randrange
import random
import wave
import contextlib

# function to add "" in our strings for tascar

def strToStr(blockname):

    return '"' + blockname + '"'

path_set="/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Sources_M"
# list of all files on the selected path with global variable .wav
set_investigated = list(Path(path_set).glob('*.wav')) 

# define paths to avoid repetition 
path_absolute = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/TASCAR_SIMULATIONS_01/"

scene_reference_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Dataset_M/Scene/References/"
scene_signal_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M/Scene/"


audio_reference_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M"
audio_signal_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M/Audio/"



for i, file_sig in enumerate(set_investigated):

    # get duration of sound file....
    with contextlib.closing(wave.open(str(file_sig),'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        # print(round(duration,2))
    
    name = str(file_sig)
    
    # ID of audio file from 1 - 42
    idx = 0

    for x_vacuum in range(7):

        for y_vacuum in range(6):
            # get string value from file_path 
            file_name = str(file_sig.stem)
            ### VACUUM
            x = x_vacuum

            y = -y_vacuum

            file_source = path_absolute + "vacuum_template.tsc"

            # Open current tsc file and read it to save it as a string

            fin = open(file_source)

            temp_receiver = fin.read()

            fin.close()

            # replace parameters in {} with whatever string you want

            vacuum = temp_receiver.format(x = x, y = y,) 

            ## SCENE-> change for anechoic and 

            file_scene = path_absolute + f'kitchen_scene_template.tsc'

            fin = open(file_scene)

            temp_scene = fin.read()

            fin.close()

            scene = temp_scene.format(vacuum = vacuum, name=name, duration=duration)


            ### CREATE TASCAR SCENE FILE -> change ref for noisy files/scenes

            file_output = scene_signal_path + file_name + "_kitchen_id_" + str(idx) + "_noise_" + str(x)+ "_" + str(y)+ "_0" + '.tsc'


            if os.path.exists(file_output):

                output = open(file_output, 'w')

            else:

                output = open(file_output, 'x')

            output.write(scene)

            output.close()

            ### RUN TASCAR
    
            audio_file = audio_signal_path + file_name + "_kitchen_id_" + str(idx) + "_noise_" + str(x)+ "_" + str(y)+ "_0"+ '.wav'

            # Run, play and save real time, need to have qjack running

            os.system(f"tascar_renderfile -o {audio_file} {file_output}")

            idx+=1        


