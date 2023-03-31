# define PACE 0
# define VB 1
# define VRP 2
# define LRLONLY 3

char pState;

main(){
    int time = 0;
    Setup();
    while(1){
        switch (pState){
        case PACE:
        processPACEState();
        break;
        case VB:
        processVBState();
        break;
        case VRP:
        processVRPState();
        break;
        case LRLONLY:
        processLRLOnlyState();
        break;
        case default:
        processError("Illegal State\n");
        break;
        }
        time++;
    }
}