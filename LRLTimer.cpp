unsigned long LRLTimerEndValue;
char timerLRLState;

void setLRLTimer(){
    LRLTimerEndValue = milis() + LRLINT;
    LRLTimerState = TIMER_SET;
    return;
}

void clearLRLTimer(){
    timerLRLState = TIMER_CLEAR;
    return;
}

char checkLRLTimer(){
    if (timerLRLState == SET){
        if (milis() < LRLTimerEndValue)
                return timerLRLState
        else timerLRLState = TIMER_EXPIRED;
    }
    return timerLRLState;
    }