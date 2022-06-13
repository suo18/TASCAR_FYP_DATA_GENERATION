import os
from pathlib import Path
import wave
import contextlib


# function to add "" in our strings for tascar

def strToStr(blockname):

    return '"' + blockname + '"'


path_set="/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Sources_M"

# define paths to avoid repetition 
path_absolute = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/TASCAR_SIMULATIONS_01/"

scene_reference_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Dataset_M/Scene/References/"
audio_reference_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Dataset_M/Audio/References/"

scene_signal_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M/Scene/"
audio_signal_path = "/Users/seth/Documents/TASCAR_FYP_DATA_GENERATION/Data_SNR_EST_M/Audio/"

# list of all files on the selected path with global variable .wav
set_investigated = list(Path(path_set).glob('*.wav')) 

x_axis = [x for x in range(-10, 10)]
y_axis = [x for x in range(-10, 10)]

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

    for i in range(len(x_axis)):
        # get string value from file_path 
        file_name = str(file_sig.stem)

        # set anechoic conditions coordinates
        x_anc = 9

        y_anc = 9

        # change coordinate of person walking 
        x = x_axis[i]

        y = y_axis[i]

        # change location of walking person 
        file_source = path_absolute + "walking_person_template.tsc"

        # Open current tsc file and read it to save it as a string

        fin = open(file_source)

        temp_receiver = fin.read()

        fin.close()

        # replace parameters in {} with whatever string you want

        receiver = temp_receiver.format(x = x, y = y,) 

        receiver_anc = temp_receiver.format(x = x_anc, y = y_anc,)

        # SAVE SCENE

        file_scene = path_absolute + f'empty_room_scene_template.tsc'

        fin = open(file_scene)

        temp_scene = fin.read()

        fin.close()

        scene = temp_scene.format(receiver = receiver, duration=duration, name=name)

        scene_anc = temp_scene.format(receiver = receiver_anc, duration=duration, name=name)

        # CREATE TASCAR SCENE FILE

        # clean scene files
        # file_output = scene_reference_path + file_name + "_empty_room_id_" + str(idx) + '.tsc'


        # if os.path.exists(file_output):

        #     output = open(file_output, 'w')

        # else:

        #     output = open(file_output, 'x')

        # output.write(scene_anc)

        # output.close()

        # save noisy scene files
        file_output_noise = scene_signal_path + file_name + "_empty_room_id_" + str(idx) + "_noise_" + str(x)+ "_" + str(y)+ "_0"+ '.tsc'

        if os.path.exists(file_output_noise):

            output = open(file_output_noise, 'w')

        else:

            output = open(file_output_noise, 'x')

        output.write(scene)

        output.close()

        ### RUN TASCAR -> save audio files 
 
        # audio_file_clean = audio_reference_path + file_name + "_empty_room_id_" + str(idx) + '.wav'

        audio_file_noisy = audio_signal_path + file_name + "_empty_room_id_" + str(idx) + "_noise_" + str(x)+ "_" + str(y)+ "_0"+ '.wav'

        # Run, play and save real time, need to have qjack running

        # os.system(f"tascar_renderfile -o {audio_file_clean} {file_output}")

        os.system(f"tascar_renderfile -o {audio_file_noisy} {file_output_noise}")

        idx+=1