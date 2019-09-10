import subprocess


def get_ds18b20_sensor(sensor_id):
    command_to_run="""cat /sys/bus/w1/devices/{0}/w1_slave""".format(sensor_id)
    output = subprocess.check_output([command_to_run], shell=True)
    raw_value = output.rsplit('=', 1)[1].strip()

    # Convert raw_value to F
    f_degrees = 1.8*float(raw_value)/1000 + 32

    return f_degrees