from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()


def howMuchToMove(yetToMove):
    move = 0
    if yetToMove < 0:
        if yetToMove > -15:
            move = yetToMove
        else:
            move = -15

        yetToMove = yetToMove - move
    else:
        if yetToMove < 15:
            move = yetToMove
        else:
            move = 15

        yetToMove = yetToMove - move

    return move, yetToMove


def moveMouse(targetX, targetY):
    currentX, currentY = mouse.position

    xToMove = targetX - currentX
    yToMove = targetY - currentY

    done = False
    while not done:
        moveX, xToMove = howMuchToMove(xToMove)
        moveY, yToMove = howMuchToMove(yToMove)

        mouse.move(moveX, moveY)
        sleep(.01)

        if(xToMove == 0 and yToMove == 0):
            done = True


# moveMouse(561, 1054)
# mouse.click(Button.left, 1)

# mouse.scroll(0, 1)
