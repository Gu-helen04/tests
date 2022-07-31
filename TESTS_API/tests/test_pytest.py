from YA_disk import YaDisk
import pytest

@pytest.mark.parametrize(
    "folder_name, result",
    [
        ('new_folder_1', True),
        ('new_folder_2', True),
        ('new_folder_1', False)
    ]
)
def test_create_folder_yandex_(folder_name, result):
    ya_token = 'AQAAAABBAA-fAADLW7Lioz_T00K0h8dHXQInC_Y'
    response = YaDisk(ya_token)
    result_func = response.create_folder_yandex_(folder_name)
    assert result == result_func