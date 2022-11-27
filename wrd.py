def wrd_cnt(wrd,paraa):
    paraa=paraa.split()
    cnt=0
    for x in paraa:
        if x.lower()==wrd.lower():
            cnt+=1
        else:
            pass
    return(cnt)

