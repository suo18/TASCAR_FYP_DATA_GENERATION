import os
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

scene_reference_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Dataset_F/Scene/References/"
audio_reference_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Dataset_F/Audio/References/"


scene_signal_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M/Scene/"
audio_signal_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M/Audio/"

x_axis = [-6, -2, 2, 6]
y_axis = [6, 3, 0, -3, -6]


for i, file_sig in enumerate(set_investigated):

    # get duration of sound file....
    with contextlib.closing(wave.open(str(file_sig),'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        # print(round(duration,2))
    
    name = str(file_sig)
    
    # ID of audio file from 1 - 20
    idx = 0

    for x_student in x_axis:

        for y_student in y_axis:
            # get string value from file_path 
            file_name = str(file_sig.stem)

            # change STUDENT

            # set height of the student -> we want to ge the same random height everytime 
            random.seed(42)
            z_student = round(1 + round(abs(random.uniform(0, 1)), 2), 2)

            file_source = path_absolute + "student_template.tsc"

            # Open current tsc file and read it to save it as a string

            fin = open(file_source)

            temp_receiver = fin.read()

            fin.close()

            # replace parameters in {} with whatever string you want

            student = temp_receiver.format(x = x_student, y = y_student, z = z_student)
            
            # create -> SCENE

            file_scene = path_absolute + f'classroom_template.tsc'

            fin = open(file_scene)

            temp_scene = fin.read()

            fin.close()

            scene = temp_scene.format(student = student, name=name, duration=duration)


            ### CREATE TASCAR SCENE FILE- > run twice for anechoic and noisy here 
            # file_output = scene_reference_path + file_name + "_classroom_id_" + str(idx) + '.tsc'

            file_output = scene_signal_path + file_name + "_classroom_id_" + str(idx) + "_noise_" + str(x_student)+ "_" + str(y_student)+ "_"+ str(z_student)+ '.tsc'


            if os.path.exists(file_output):

                output = open(file_output, 'w')

            else:

                output = open(file_output, 'x')

            output.write(scene)

            output.close()

            ## RUN TASCAR -> save audio files but do twice for noisy and clean 

            # audio_file = audio_reference_path + file_name + "_classroom_id_" + str(idx) +'.wav'


            audio_file = audio_signal_path + file_name + "_classroom_id_" + str(idx) + "_noise_" + str(x_student)+ "_" + str(y_student)+ "_"+ str(z_student)+ '.wav'


            # Run, play and save real time, need to have qjack running


            os.system(f"tascar_renderfile -o {audio_file} {file_output}") 

            idx+=1








