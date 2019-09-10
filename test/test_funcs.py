from pi_funcs.funcs import get_ds18b20_sensor
from unittest import TestCase, mock


class FuncsTestCase(TestCase):
    @mock.patch('subprocess.check_output', return_value="t=28625")
    def test_get_temp(self, mock_temp_call):
        temp_reading = get_ds18b20_sensor('abcdef', 27)
        self.assertEqual(83.525, temp_reading)
        mock_temp_call.assert_called_once_with(['cat /sys/bus/w1/devices/abcdef/w1_slave'], shell=True)
