def weekday(number,optional):
    """
    This helper function will be used to return the day
    of the week"""
    
    day = optional.capitalize()
    if number == 0:
        return day
    if number <= 7:
        modulo = number
    elif number > 7:
        modulo = number%7
    



    Sunday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    Monday = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
    Tuesday = ["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"]
    Wednesday = ["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
    Thursday = ["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]
    Friday = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    Saturday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


    if day == "Sunday":
        count = 0
        for i in Sunday:
            count += 1
            if count == modulo:
                return i
            

    if day == "Monday":
        count = 0
        for i in Monday:
            count += 1
            if count == modulo:
                return i

    if day == "Tuesday":
        count = 0
        for i in Tuesday:
            count += 1
            if count == modulo:
                return i

    if day == "Wednesday":
        count = 0
        for i in Wednesday:
            count += 1
            if count == modulo:
                return i

    if day == "Thursday":
        count = 0
        for i in Thursday:
            count += 1
            if count == modulo:
                return i

    if day == "Friday":
        count = 0
        for i in Friday:
            count += 1
            if count == modulo:
                return i

    if day == "Saturday":
        count = 0
        for i in Saturday:
            count += 1
            if count == modulo:
                return i
                
        



def add_time(start,duration,optional = None):
    first = start.split()
    second = duration.split(":")
    start_hour = first[0]
    time = first[1]

    if optional == None:

        if time == "PM" and int(second[0]) >= 24:
            partition = start_hour.split(":")
            days = int(second[0])//24
            hours = int(second[0])%24
            add = int(partition[0])
            n = 0
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1]+"+"+second[1])
            if partition[0] == "12":
                distance = 12
                if hours >= distance:
                    add = hours - distance
                    time = "AM"
                    n += 1
                    if add >= 12:
                        add = add - 12
                        time = "PM"
                        
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "PM"
                            
                elif minutes >= 60:
                    floor = minutes//60
                    hours = hours + floor
                    minutes = minutes%60
                    if hours >= distance:
                        add = hours - distance
                        time = "AM"
                        n += 1
                        if add >= 12:
                            add = add - 12
                            time = "PM"
                            
                    else:
                        add = (add + hours) - 12
                else:
                    add = 0 + hours
                        
                    
                    
            else:
                distance = 12 - add
                if hours >= distance:
                    add = hours - distance
                    time = "AM"
                    n += 1
                    if add >= 12:
                        add = add - 12
                        time = "PM"
                        
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "PM"
                            
                else:
                    if minutes >= 60:
                        floor = minutes//60
                        hours = hours + floor
                        minutes = minutes%60
                        distance = 12 - add
                        if hours >= distance:
                            add = hours - distance
                            time = "AM"
                            n += 1
                        else:
                            add = add + hours
                        
                        
                
            if minutes >= 60:
                floor = minutes//60
                add = add + floor
                minutes = minutes%60
            
            if minutes < 10:
                minutes = "0" + str(minutes)

            if n == 1:
                days = days + n

            if add == 0:
                add = 12
                
            if days == 1:
                return "{}:{} {} (next day)".format(add,minutes,time)
                
            else:
                return "{}:{} {} ({} days later)".format(add,minutes,time,days)
                
            

        if time == "AM" and int(second[0]) >= 24:
            partition = start_hour.split(":")
            days = int(second[0])//24
            hours = int(second[0])%24
            add = int(partition[0])
            n = 0
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1]+"+"+second[1])
            if partition[0] == "12":
                distance = 12
                if hours >= distance:
                    add = hours - distance
                    time = "PM"
                    if add >= 12:
                        add = add - 12
                        time = "AM"
                        n += 1
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "AM"
                            n += 1
                elif minutes >= 60:
                    floor = minutes//60
                    hours = hours + floor
                    minutes = minutes%60
                    if hours >= distance:
                        add = hours - distance
                        time = "PM"
                        if add >= 12:
                            add = add - 12
                            time = "AM"
                            n += 1
                    else:
                        add = (add + hours) - 12
                else:
                    add = 0 + hours
                        
                    
                    
            else:
                distance = 12 - add
                if hours >= distance:
                    add = hours - distance
                    time = "PM"
                    if add >= 12:
                        add = add - 12
                        time = "AM"
                        n += 1
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "AM"
                            n += 1
                else:
                    if minutes >= 60:
                        floor = minutes//60
                        hours = hours + floor
                        minutes = minutes%60
                        distance = 12 - add
                        if hours >= distance:
                            add = hours - distance
                            time = "PM"
                        else:
                            add = add + hours
                        
                
            if minutes >= 60:
                floor = minutes//60
                add = add + floor
                minutes = minutes%60
            
            if minutes < 10:
                minutes = "0" + str(minutes)

            if n == 1:
                days = days + n

            if add == 0:
                add = 12
                
            if days == 1:
                return "{}:{} {} (next day)".format(add,minutes,time)
                
            else:
                return "{}:{} {} ({} days later)".format(add,minutes,time,days)
            

        if time == "PM" and int(second[0]) < 24:
            partition = start_hour.split(":")
            add = eval(partition[0]+ " + "+second[0])
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1] + " + "+second[1])
            n = 0
            if int(second[0]) >= 12:
                if partition[0] == "12":
                    time = "AM"
                    hours = 24
                    add = int(second[0]) - int(partition[0])
                    n += 1
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add == 12:
                            time = "PM"
                            n += 1
                        if add > 12:
                            time = "PM"
                            n += 1
                            add = add - 12
                        if minutes < 10:
                            minutes = "0" + str(minutes)

                else:
                    hours = 12 - int(partition[0])
                    if int(second[0]) >= hours:
                        add = int(second[0]) - hours
                        time = "AM"
                        n += 1
                        if minutes >= 60:
                            floor = minutes//60
                            add = add + floor
                            minutes = minutes%60
                        if add >= 12:
                            time = "PM"
                            add = add - 12
                            n += 1
                            
                
                                
                if add == 0:
                    add = 12
                              
                              
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)
                    
                if int(minutes) >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if minutes < 10:
                        minutes = "0" + str(minutes)

                if n >= 1:
                    n = "next day"
                    return "{}:{} {} ({})".format(add,minutes,time,n)
                else:
                    return "{}:{} {}".format(add,minutes,time)
                
                        
            elif int(second[0]) < 12:
                if add >= 12 and partition[0] == "12":
                    time = "PM"
                    add = add -12
                elif add >= 12:
                    time = "AM"
                    add = add - 12
                    n += 1
                    
                if minutes >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if add == 12:
                        time = "AM"
                        n += 1
                    if add > 12:
                        time = "AM"
                        add = add - 12
                        n += 1
                    if minutes < 10:
                        minutes = "0" + str(minutes)
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)

                if add == 0:
                    add = 12
                
                if n == 1:
                    n = "next day"
                    return "{}:{} {} ({})".format(add,minutes,time,n)
                else:
                    return "{}:{} {}".format(add,minutes,time)
                    
                    


        if time == "AM" and int(second[0]) < 24:
            partition = start_hour.split(":")
            add = eval(partition[0]+" + "+second[0])
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1] + " + "+second[1])
            n = 0
            
            if int(second[0]) >= 12:
                if partition[0] == "12":
                    time = "PM"
                    hours = 24
                    add = int(second[0]) - int(partition[0])
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add == 12:
                            time = "AM"
                            n += 1
                        if add > 12:
                            time = "AM"
                            n += 1
                            add = add - 12
                        if minutes < 10:
                            minutes = "0" + str(minutes)

                else:
                    hours = 12 - int(partition[0])
                    if int(second[0]) >= hours:
                        add = int(second[0]) - hours
                        time = "PM"
                        if minutes >= 60:
                            floor = minutes//60
                            add = add + floor
                            minutes = minutes%60
                        if add >= 12:
                            time = "AM"
                            add = add - 12
                            n += 1
                            
                
                                
                if add == 0:
                    add = 12
                              
                              
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)
                    
                if int(minutes) >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if minutes < 10:
                        minutes = "0" + str(minutes)

                if n == 1:
                    n = "next day"
                    return "{}:{} {} ({})".format(add,minutes,time,n)
                else:
                    return "{}:{} {}".format(add,minutes,time)
                              
                              
            elif int(second[0]) < 12:
                if add >= 12 and partition[0] == "12":
                    time = "AM"
                    add = add -12
                elif add >= 12:
                    time = "PM"
                    add = add - 12
                if minutes >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if add == 12:
                        time = "PM"
                    if add > 12:
                        time = "PM"
                        add = add - 12
                    if minutes < 10:
                        minutes = "0" + str(minutes)
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)

                if add == 0:
                    add = 12

                return "{}:{} {}".format(add,minutes,time)
                


    elif optional != None:

        if time == "PM" and int(second[0]) >= 24:
            partition = start_hour.split(":")
            days = int(second[0])//24
            hours = int(second[0])%24
            add = int(partition[0])
            n = 0
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1]+"+"+second[1])
            if partition[0] == "12":
                distance = 12
                if hours >= distance:
                    add = hours - distance
                    time = "AM"
                    n += 1
                    if add >= 12:
                        add = add - 12
                        time = "PM"
                        
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "PM"
                            
                elif minutes >= 60:
                    floor = minutes//60
                    hours = hours + floor
                    minutes = minutes%60
                    if hours >= distance:
                        add = hours - distance
                        time = "AM"
                        n += 1
                        if add >= 12:
                            add = add - 12
                            time = "PM"
                            
                    else:
                        add = (add + hours) - 12
                else:
                    add = 0 + hours
                        
                    
                    
            else:
                distance = 12 - add
                if hours >= distance:
                    add = hours - distance
                    time = "AM"
                    n += 1
                    if add >= 12:
                        add = add - 12
                        time = "PM"
                        
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "PM"
                            
                else:
                    if minutes >= 60:
                        floor = minutes//60
                        hours = hours + floor
                        minutes = minutes%60
                        distance = 12 - add
                        if hours >= distance:
                            add = hours - distance
                            time = "AM"
                            n += 1
                        else:
                            add = add + hours
                        
                        
                
            if minutes >= 60:
                floor = minutes//60
                add = add + floor
                minutes = minutes%60
            
            if minutes < 10:
                minutes = "0" + str(minutes)

            if n == 1:
                days = days + n

            if add == 0:
                add = 12

            week_day = weekday(days,optional)
                
            if days == 1:
                return "{}:{} {}, {} (next day)".format(add,minutes,time,week_day)
                
            else:
                return "{}:{} {}, {} ({} days later)".format(add,minutes,time,week_day,days)
                
            

        if time == "AM" and int(second[0]) >= 24:
            partition = start_hour.split(":")
            days = int(second[0])//24
            hours = int(second[0])%24
            add = int(partition[0])
            n = 0
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1]+"+"+second[1])
            if partition[0] == "12":
                distance = 12
                if hours >= distance:
                    add = hours - distance
                    time = "PM"
                    if add >= 12:
                        add = add - 12
                        time = "AM"
                        n += 1
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "AM"
                            n += 1
                elif minutes >= 60:
                    floor = minutes//60
                    hours = hours + floor
                    minutes = minutes%60
                    if hours >= distance:
                        add = hours - distance
                        time = "PM"
                        if add >= 12:
                            add = add - 12
                            time = "AM"
                            n += 1
                    else:
                        add = (add + hours) - 12
                else:
                    add = 0 + hours
                        
                    
                    
            else:
                distance = 12 - add
                if hours >= distance:
                    add = hours - distance
                    time = "PM"
                    if add >= 12:
                        add = add - 12
                        time = "AM"
                        n += 1
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add >= 12:
                            add = add - 12
                            time = "AM"
                            n += 1
                else:
                    if minutes >= 60:
                        floor = minutes//60
                        hours = hours + floor
                        minutes = minutes%60
                        distance = 12 - add
                        if hours >= distance:
                            add = hours - distance
                            time = "PM"
                        else:
                            add = add + hours
                        
                
            if minutes >= 60:
                floor = minutes//60
                add = add + floor
                minutes = minutes%60
            
            if minutes < 10:
                minutes = "0" + str(minutes)

            if n == 1:
                days = days + n

            if add == 0:
                add = 12

            week_day = weekday(days,optional)

            if days == 1:
                return "{}:{} {}, {} (next day)".format(add,minutes,time,week_day)
                
            else:
                return "{}:{} {}, {} ({} days later)".format(add,minutes,time,week_day,days)
            
                
           
            

        if time == "PM" and int(second[0]) < 24:
            partition = start_hour.split(":")
            add = eval(partition[0]+ " + "+second[0])
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1] + " + "+second[1])
            n = 0
            if int(second[0]) >= 12:
                if partition[0] == "12":
                    time = "AM"
                    hours = 24
                    add = int(second[0]) - int(partition[0])
                    n += 1
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add == 12:
                            time = "PM"
                            n += 1
                        if add > 12:
                            time = "PM"
                            n += 1
                            add = add - 12
                        if minutes < 10:
                            minutes = "0" + str(minutes)

                else:
                    hours = 12 - int(partition[0])
                    if int(second[0]) >= hours:
                        add = int(second[0]) - hours
                        time = "AM"
                        n += 1
                        if minutes >= 60:
                            floor = minutes//60
                            add = add + floor
                            minutes = minutes%60
                        if add >= 12:
                            time = "PM"
                            add = add - 12
                            n += 1
                            
                
                                
                if add == 0:
                    add = 12
                              
                              
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)
                    
                if int(minutes) >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if minutes < 10:
                        minutes = "0" + str(minutes)

                if n >= 1:
                    days = 1

                week_day = weekday(days,optional)
                

                return "{}:{} {}, {} (next day)".format(add,minutes,time,week_day)
                
                        
            elif int(second[0]) < 12:
                if add >= 12 and partition[0] == "12":
                    time = "PM"
                    add = add -12
                elif add >= 12:
                    time = "AM"
                    add = add - 12
                    n += 1
                    
                if minutes >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if add == 12:
                        time = "AM"
                        n += 1
                    if add > 12:
                        time = "AM"
                        add = add - 12
                        n += 1
                    if minutes < 10:
                        minutes = "0" + str(minutes)
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)

                if add == 0:
                    add = 12
                
                if n == 1:
                    days = 1
                else:
                    days = 0

                week_day = weekday(days,optional)
                

                if days == 1:
                    return "{}:{} {}, {} (next day)".format(add,minutes,time,week_day)
                else:
                    return "{}:{} {}, {}".format(add,minutes,time,week_day)
                    
                    


        if time == "AM" and int(second[0]) < 24:
            partition = start_hour.split(":")
            add = eval(partition[0]+" + "+second[0])
            if second[1].startswith("0"):
                second[1] = second[1][1]
            if partition[1].startswith("0"):
                partition[1] = partition[1][1]
            minutes = eval(partition[1] + " + "+second[1])
            n = 0
            
            if int(second[0]) >= 12:
                if partition[0] == "12":
                    time = "PM"
                    hours = 24
                    add = int(second[0]) - int(partition[0])
                    if minutes >= 60:
                        floor = minutes//60
                        add = add + floor
                        minutes = minutes%60
                        if add == 12:
                            time = "AM"
                            n += 1
                        if add > 12:
                            time = "AM"
                            n += 1
                            add = add - 12
                        if minutes < 10:
                            minutes = "0" + str(minutes)

                else:
                    hours = 12 - int(partition[0])
                    if int(second[0]) >= hours:
                        add = int(second[0]) - hours
                        time = "PM"
                        if minutes >= 60:
                            floor = minutes//60
                            add = add + floor
                            minutes = minutes%60
                        if add >= 12:
                            time = "AM"
                            add = add - 12
                            n += 1
                            
                
                                
                if add == 0:
                    add = 12
                              
                              
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)
                    
                if int(minutes) >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if minutes < 10:
                        minutes = "0" + str(minutes)

                if n == 1:
                    days = 1
                else:
                    days = 0

                week_day = weekday(days,optional)
                

                if days == 1:
                    return "{}:{} {}, {} (next day)".format(add,minutes,time,week_day)
                else:
                    return "{}:{} {}, {}".format(add,minutes,time,week_day)
                              
                              
            elif int(second[0]) < 12:
                if add >= 12 and partition[0] == "12":
                    time = "AM"
                    add = add -12
                elif add >= 12:
                    time = "PM"
                    add = add - 12
                if minutes >= 60:
                    floor = minutes//60
                    add = add + floor
                    minutes = minutes%60
                    if add == 12:
                        time = "PM"
                    if add > 12:
                        time = "PM"
                        add = add - 12
                    if minutes < 10:
                        minutes = "0" + str(minutes)
                if len(str(minutes)) == 1:
                    minutes = "0" + str(minutes)

                if add == 0:
                    add = 12

                days = 0

                week_day = weekday(days,optional)

                return "{}:{} {}, {}".format(add,minutes,time,week_day)
                              

               
        
    
        
   







        
