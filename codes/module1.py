
def convert_to_24hrs(string_time):
    if ((string_time.find('am'))==-1):
        time_lst=list(string_time)
        time_lst.remove(':')
        time_lst.remove('p')
        time_lst.remove('m')
        time_lst.insert(0,'0')
        delimiter='' 
        time_val=delimiter.join(time_lst)
        time_24=int(time_val)
        if time_24>=1200 and time_24<= 1259:
            pass
        else:
            time_24 += 1200
        return time_24
    if ((string_time.find('pm'))==-1):
        time_lst=list(string_time)
        time_lst.remove(':')
        time_lst.remove('a')
        time_lst.remove('m')
        time_lst.insert(0,'0')
        delimiter='' 
        time_val=delimiter.join(time_lst)
        time_24=(int(time_val))
        return time_24

def GetTimePeriod(line):
    space_pos=line.find(' ')
    dash_pos=line.find('-')
    m_pos=line.find('m',dash_pos)
    data=line[space_pos:m_pos+1]
    return data

def Time_spent(start,end):
    strt=str(start)
    stp=str(end)
    a=int(strt[:len(strt)-2])
    b=int(strt[len(strt)-2:])
    c=int(stp[:len(stp)-2])
    d=int(stp[len(stp)-2:])
    if (d < b):
        f=((60+d)-b)
        c-=1
        e=(c-a)
        e=str(e)
        f=str(f)
        answer=int(e+f)
        return answer
    if(d>b):
        f=(d-b)
        if (a==12):
            a=0
        e=(c-a)
        e=str(e)
        f=str(f)
        answer=int(e+f)
        return answer
    if(d==b):
        f=(d-b)
        if (c==12 and c>a):
            c=12
        if (c==12 and c<a):
            c=24
        e=(c-a)
        e=str(e)
        f=str(f)
        answer=int(e+f)
        answer=answer*10
        return answer

    


def GetTimeValue(data):
    #obtain the start time
    sppos=data.find(' ')
    first_m=data.find('m',sppos)
    start_time=data[sppos+1:first_m+1]
    #obtain the stop time
    dash_pos=data.find('-')
    m_pos=data.find('m',dash_pos)
    end_time=data[dash_pos+1:m_pos+1]
    start_time=start_time.strip()
    end_time=end_time.strip()

    START=convert_to_24hrs(start_time)
    END=convert_to_24hrs(end_time)
    return Time_spent(START,END)

def hours_time(acc_time):
    acc_time = str(acc_time)
    a=acc_time[:(len(acc_time)-2)]
    if len(a)>0:
        a=int(a)
        return a
    else:
        return 0


def minutes_time(acc_time):
    acc_time = str(acc_time)
    b=acc_time[len(acc_time)-2:]
    if len(b)>0:
        b=int(b)
        return b
    else:
        return 0
