import pytest
from main import existence_check, get_name, get_shelf, add_data, delete_data, cut_and_paste, add_shelf


class TestFunction:

    @pytest.mark.parametrize(
        "document_number, result",
        [
            ('10006', 'Аристарх Павлов'),
            ('11-2', 'Геннадий Покемонов'),
            ('11111', None)
        ]
    )
    def test_get_name(self, document_number, result):
        result_func = get_name(document_number)
        assert result_func == result

    @pytest.mark.parametrize(
        "document_number,result ",
        [
            ('10006', 2),
            ('11-2', 1),
            ('111111', None)
        ]
    )
    def test_get_shelf(self, document_number, result):
        result_func = get_shelf(document_number)
        assert result_func == result

    @pytest.mark.parametrize(
        "number_doc, result",
        [
            ('10006', [{'name': 'Василий Гупкин', 'number': '2207 876234', 'type': 'passport'},
                       {'name': 'Геннадий Покемонов', 'number': '11-2', 'type': 'invoice'}])
        ]
    )
    def test_delet_data(self, number_doc, result):
        result_func = delete_data(number_doc)
        assert result_func == result

    @pytest.mark.parametrize(
        "shelf_number, name_doc, number_doc, full_name, result",
        [
            ('2', 'pass', '1234', 'Rick', [{'name': 'Василий Гупкин', 'number': '2207 876234', 'type': 'passport'},
                                           {'name': 'Геннадий Покемонов', 'number': '11-2', 'type': 'invoice'},
                                           {'name': 'Rick', 'number': '1234', 'type': 'pass'}])
        ]
    )
    def test_add_data(self, shelf_number, name_doc, number_doc, full_name, result):
        result_func = add_data(shelf_number, name_doc, number_doc, full_name)
        assert result_func == result

    @pytest.mark.parametrize(
        "numb_shelf, numb_doc, result",
        [
            ('3', '1234', {'1': ['2207 876234', '11-2', '5455 028765',], '2': [], '3': ['1234']})
        ]
    )
    def test_cut_and_pust(self, numb_doc, numb_shelf, result):
        result_func = cut_and_paste(numb_doc, numb_shelf)
        assert result_func == result

    @pytest.mark.parametrize(
        "numb_shelf, result",
        [
            ('4', {'1': ['2207 876234', '11-2', '5455 028765',], '2': [], '3': ['1234'], '4': []})
        ]
    )
    def test_add_shelf(self, numb_shelf, result):
        result_func = add_shelf(numb_shelf)
        assert result_func == result

    @pytest.mark.parametrize(
        "document_number, shelf_number, result",
        [
            ('11-2', 0, True),
            (0, '4', True),
            (0, '5', False),
            ('4653543', 0, False)
        ]
    )
    def test_existence_check(self, document_number, shelf_number, result):
        result_func = existence_check(document_number, shelf_number)
        assert result_func == result
