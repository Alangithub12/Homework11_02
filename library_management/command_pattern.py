# command_pattern.py

class Command:
    def execute(self):
        pass

class Light:
    def turn_on(self):
        return "Свет включен."

    def turn_off(self):
        return "Свет выключен."

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        return self.command.execute()

# Пример использования
if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.set_command(light_on)
    print(remote.press_button())  # Вывод: Свет включен.

    remote.set_command(light_off)
    print(remote.press_button())  # Вывод: Свет выключен.