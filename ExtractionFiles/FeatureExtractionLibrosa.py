# Feature extraction example
import os

import  scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import numpy as np






count = 0
f = open("Data/data.csv","w")
# composer_number_values = {"Barenboim":1,"Denk":2,"Dinnerstein":3,"Gould":4,"Hewitt":5,"Kempff":6,"Perahia":7}
#loop through every song, divide song into segments,extract features from each segment
#each segment from one song belongs to the same class
for root, dirs, song_files in os.walk("AudioFiles/"):
    for file in song_files:
        #start offset and duration
        offset = 0
        feature_extraction_duration = 20
        duration = librosa.get_duration(filename="AudioFiles/"+file)
        grade = None

        #write features for every segment
        #every segment of a song belongs to the same class
        while(offset<duration):
            # Load the example clip

            y, sr = librosa.load("AudioFiles/"+file,duration=feature_extraction_duration,offset=offset)


            feature_values = dict()
            offset = 6
            #get level of song
            while(filename[len(filename)-offset]!='('):
                char =  filename[len(filename)-offset]
                char+=num
                num = char
                offset+=1
            grade = int(num)
            
            print("offset: ",offset,"   duration: ",duration, "  grade: ",grade)


            # Set the hop length; at 22050 Hz, 512 samples ~= 23ms
            hop_length = 512

            ####
            #useful for audio matching and similarity
            chrom_cens = librosa.feature.chroma_cens(y, sr=sr, hop_length=hop_length)
            index = 0
            max_array = []
            for row in chrom_cens:
                #print("chroma_cens: ", np.average(chrom_cens[index]), end="\n\n\n\n\n\n\n\n\n\n")
                feature = "chroma_cens"+str(index)
                feature_values[feature] = np.average(chrom_cens[index])
                index+=1

            feature_values["chroma_cens_max"] = np.amax(chrom_cens)



            ####
            chrom_stft = librosa.feature.chroma_stft(y, sr=sr, hop_length=hop_length)
            index = 0
            for row in chrom_stft:
                #print("chrom_stft: ", np.average(chrom_stft[index]), end="\n\n\n\n\n\n\n\n\n\n")
                feature = "chrom_stft"+str(index)
                feature_values[feature] = np.average(chrom_stft[index])
                index+=1

            ####
            chrom_cqt = librosa.feature.chroma_cqt(y, sr=sr, hop_length=hop_length)
            index = 0
            for row in chrom_cqt:
                #print("chrom_cqt: ", np.average(chrom_cqt[index]), end="\n\n\n\n\n\n\n\n\n\n")
                feature = "chrom_cqt"+str(index)
                feature_values[feature] = np.average(chrom_cqt[index])
                index+=1

            #
            # mfcc = librosa.feature.mfcc(y, sr=sr, hop_length=hop_length)
            # index = 0
            # for row in mfcc:
            #     print("mfcc: ", np.average(mfcc[index]), end="\n\n\n\n\n\n\n\n\n\n")
            #     feature = "mfcc"+str(index)
            #     feature_values[feature] = np.average(mfcc[index])
            #     index+=1

            #
            # mel_spec = librosa.feature.melspectrogram(y, sr=sr, hop_length=hop_length)
            # plt.figure(figsize=(10, 4))
            # S_dB = librosa.power_to_db(mel_spec, ref=np.max)
            # librosa.display.specshow(S_dB, x_axis='time',
            #                           y_axis='mel', sr=sr,
            #                           fmax=8000)
            # plt.colorbar(format='%+2.0f dB')
            # plt.title('Mel-frequency spectrogram')
            # plt.tight_layout()
            # plt.show()

            ####
            spect_flatness = librosa.feature.spectral_flatness(y, hop_length=hop_length)
            feature = "spect_flatness_avg"
            feature_values[feature] = np.average(spect_flatness)
            #print(np.average(spect_flatness))


            ####
            zcr = librosa.feature.zero_crossing_rate(y)
            feature = "zcr"
            feature_values[feature] = np.average(zcr)

            #plt.figure(figsize=(15, 5))
            #librosa.display.specshow(chrom_cens, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
            #print("\n\n")


            # print("chroma_stft: ", chrom_stft, end="\n\n\n\n\n\n\n\n\n\n")
            # print("chroma_cqt: ", chrom_cqt, end="\n\n\n\n\n\n\n\n\n\n")
            # print("mfcc: ", mfcc, end="\n\n\n\n\n\n\n\n\n\n")
            # print("melspectrogram: ", mel_spec, end="\n\n\n\n\n\n\n\n\n\n")
            # print("spectral_flatness: ", spect_flatness, end="\n\n\n\n\n\n\n\n\n\n")
            # print("zero_crossing_rate: ", zcr, end="\n\n\n\n\n\n\n\n\n\n")
            #plt.show()
            #print(beat_features)


            #write features in file
            if count==0:
                for feature in feature_values:
                    f.write(feature+",")
                f.write("Grade")
                f.write("\n")

            #write feature values
            for feature,value in feature_values.items():
                val = str(value)+","
                f.write(val)
            f.write(str(grade))
            f.write("\n")

    
            count+=1
            offset+=feature_extraction_duration
