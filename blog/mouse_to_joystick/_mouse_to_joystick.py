import evdev
import uinput

RANGE = 65536  # 0 - 65535
HALF_RANGE = RANGE // 2


def main():
    # Search for all connected input devices
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    # Find a mouse
    mouse = None
    for device in devices:
        if "mouse" in device.name.lower():
            mouse = device
            break

    print(mouse.capabilities(verbose=True))

    # Create a simple joystick with two main axes
    joystick = (
        uinput.ABS_X + (-HALF_RANGE, HALF_RANGE, 0, 0),
        uinput.ABS_Y + (-HALF_RANGE, HALF_RANGE, 0, 0),
    )

    # Read mouse events and convert them to joystick inputs
    with uinput.Device(joystick) as j:
        for event in mouse.read_loop():  # runs in a constant loop
            if event.type == evdev.ecodes.EV_ABS:
                if event.code == evdev.ecodes.ABS_X:
                    print("X:", event.value - HALF_RANGE)
                    j.emit(uinput.ABS_X, event.value - HALF_RANGE)

                if event.code == evdev.ecodes.ABS_Y:
                    print("Y:", event.value - HALF_RANGE)
                    j.emit(uinput.ABS_Y, event.value - HALF_RANGE)


if __name__ == "__main__":
    main()
