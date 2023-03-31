#define TIMER_SET 0
#define TIMER_CLEAR 1
#define TIMER_EXPIRED 2

void processLRLOnlyState(){
    if (checkLRLTimer() == TIMER_EXPIRED{}){
    /* Start LRLTimer */
    clearLRLTimer();
    setLRLTimer();
    /* If LRLTimer expires, next state is PACE */
    pState = PACE;
    VPaceOn();
    setVPACETimer();
    return;
    }
    if (IsVentricularEvent()){
    /* Start LRLTimer */
    clearLRLTimer();
    setLRLTimer();
    /* If sense a R wave, then next state is state VB */
    pState = VB;
    return;
    }
    return;
}