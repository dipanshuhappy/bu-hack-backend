def getCoinAmount(least_mark:int,highest_mark:int,student_mark:int,max_coin:int):
    if(least_mark==highest_mark):
        return 1
    return round((((student_mark-least_mark)*max_coin)/(highest_mark-least_mark)))