from hub import port, motion_sensor
import runloop, motor_pair, sys
# cm, this is a constant for your robot
WHEEL_CIRCUMFERENCE = 17.5
# input must be in the same unit as WHEEL_CIRCUMFERENCE
def degreesForDistance(distance_cm):
# Add multiplier for gear ratio if needed
    return int((distance_cm/WHEEL_CIRCUMFERENCE) * 360)
async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)
    async def Girar(direccion):
        motion_sensor.reset_yaw(0)
        await runloop.sleep_ms(1000)
        if direccion == 'derecha': # Giro Derecho
            while motion_sensor.tilt_angles()[0] > -900:
                motor_pair.move(motor_pair.PAIR_1, 100)
            motor_pair.stop(motor_pair.PAIR_1)
            motion_sensor.reset_yaw(0)
        elif direccion == 'izquierda': # Giro Izquierdo
            while motion_sensor.tilt_angles()[0] < 900:
                motor_pair.move(motor_pair.PAIR_1, -100)
            motor_pair.stop(motor_pair.PAIR_1)
            motion_sensor.reset_yaw(0)
        else:
            sys.exit()

    async def Mover(direccion):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, degreesForDistance(direccion), 0)
# Drive Base 1
    

    await Mover(20)
    await Girar('derecha')
    await Mover(20)
    await Girar('izquierda')
    await Mover(40)
    await Girar('izquierda')
    await Mover(20)
    await Girar('izquierda')
    await Mover(40)


    sys.exit()
runloop.run(main())