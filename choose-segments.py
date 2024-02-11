def cal_duration(threshould : int):
    file = open("align_with_text.csv" , "r")
    lines = file.readlines()
    lines[0]=  ""
    comma_before_end = 3
    comma_before_score = 1
    high_score_length = 0
    audio_length = 0
    min_to_sec = 60
    for line in lines:
        if(line == ""):
            continue
        comma_counter = 0
        high_duration = 0.0
        hole_duration = 0.0
        end_time_dur = ""
        score_dur = ""
        score=0
        for letter in line:
            if(letter == ','):
                comma_counter+=1

            if(comma_counter == comma_before_score and letter!=","):
                score_dur+=letter
            elif(comma_counter == comma_before_score+1):
                score = int(score_dur)

            elif(comma_counter == comma_before_end and letter!=","):
                end_time_dur += letter
            elif(comma_counter == comma_before_end+1):
                if(score > threshould):     
                    high_duration += float(end_time_dur)
                hole_duration += float(end_time_dur)
                break
        high_score_length += high_duration
        audio_length += hole_duration
    return high_score_length/min_to_sec , audio_length/min_to_sec , (high_score_length/audio_length)
res , hole , percentage = (cal_duration(90))
print("Original duration : " , "%.2f"%hole , "min")
print("High score segments : " , "%.2f"%res ,"min", "(","%.2f"%(percentage*100),"% )")