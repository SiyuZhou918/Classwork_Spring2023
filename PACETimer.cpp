unsigned long paceTimerEndValue;
char timerPaceState;

/* Function to set the PaceTimer */
void setPaceTimer() {
    /* Set the end time */
    paceTimerEndValue = millis() + PACEINT;
    /* Set the time state */
    timerPaceState = TIMER_SET;
}

/* Function to clear the PaceTimer */
void clearPaceTimer() {
    /* Set the time state */
    timerPaceState = TIMER_CLEAR;
}

/* Function to check the PaceTimer */
char checkPaceTimer() {
    if (timerPaceState == TIMER_SET) {
        /* Check if the current time is less than the end time */
        if (millis() < paceTimerEndValue) {
            /* If it is, return the timer state (TIMER_SET) */
            return timerPaceState;
        } else {
            /* If it's not, set the timer state to TIMER_EXPIRED */
            timerPaceState = TIMER_EXPIRED;
        }
    }
    /* Return the timer state (either TIMER_SET or TIMER_EXPIRED) */
    return timerPaceState;
}