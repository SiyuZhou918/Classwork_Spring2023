#define TIMER_SET 0
#define TIMER_CLEAR 1
#define TIMER_EXPIRED 2

void processPACEState(){
    if (checkVPaceTimer() == TIMER_EXPIRED{}){
    /* Start VPACETimer */
    clearVPACETimer();
    setVPACETimer();
    /* If VPaceTimer expires, next state is VB */
    pState = VB;
    VPaceOff();
    /* Setup everything needed for state VB */
    setVBTimer();
    return;
    }
    return;
}

void processVBState(){
    if (checkVBTimer() == TIMER_EXPIRED{}){
    /* Start VBTimer */
    clearVBTimer();
    setVBTimer();
    /* If VBTimer expires, next state is VRP */
    pState = VRP;
    VPaceOff();
    /* Setup everything needed for state VRP */
    setVRPTimer();
    return;
    }
    return;
}

void processVRPState(){
    if (checkVRPTimer() == TIMER_EXPIRED{}){
    /* Start VRPTimer */
    clearVRPTimer();
    setVRPTimer();
    /* If VRPTimer expires, next state is LRLONLY */
    pState = LRLONLY;
    /* Setup everything needed for state LRLONLY */
    setLRLTimer();
    return;
    }
    return;
}