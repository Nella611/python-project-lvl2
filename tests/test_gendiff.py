#!/usr/bin/env python3
import os
import pytest
from gendiff import generate_diff


dirname = os.path.dirname(__file__)
first_json_file = os.path.join(dirname, 'fixtures/file1.json')
second_json_file = os.path.join(dirname, 'fixtures/file2.json')
first_yaml_file = os.path.join(dirname, 'fixtures/file1.yml')
second_yaml_file = os.path.join(dirname, 'fixtures/file2.yaml')
first_branching_file = os.path.join(dirname, 'fixtures/file1_branching.json')
second_branching_file = os.path.join(dirname, 'fixtures/file2_branching.json')
first_yaml_branching_file = os.path.join(dirname, 'fixtures/file1_branching.yaml')
second_yaml_branching_file = os.path.join(dirname, 'fixtures/file2_branching.yml')
first_empty_json_file = os.path.join(dirname, 'fixtures/empty_json1.json')
second_empty_json_file = os.path.join(dirname, 'fixtures/empty_json1.json')

parameters_mark = [
    (first_json_file, second_json_file, 'stylish', 'fixtures/answer_for_stylish_flat'),
    (first_yaml_file, second_yaml_file, 'stylish', 'fixtures/answer_for_stylish_flat'),
    (first_branching_file, second_branching_file, 'plain', 'fixtures/answer_for_plain_branching'),
    (first_branching_file, second_branching_file, 'stylish', 'fixtures/answer_for_stylish_branching'),
    (first_yaml_branching_file, second_yaml_branching_file, 'stylish', 'fixtures/answer_for_stylish_branching'),
    (first_branching_file, second_branching_file, 'json', 'fixtures/answer_for_json'),
    (first_yaml_branching_file, second_yaml_branching_file, 'plain', 'fixtures/answer_for_plain_branching'),
    (first_yaml_branching_file, second_yaml_branching_file, 'json', 'fixtures/answer_for_json'),
    (first_empty_json_file, second_empty_json_file, 'json', 'fixtures/answer_for_empty_json'),
]


@pytest.mark.parametrize(('ff, sf, format, answer'), parameters_mark)
def test_generate_diff_json(ff, sf, format, answer):
    with open(os.path.join(dirname, answer)) as answer:
        assert generate_diff(ff, sf, format) == answer.read()


empty_f1 = os.path.join(dirname, 'fixtures/empty_file1')
empty_f2 = os.path.join(dirname, 'fixtures/empty_file2')
parameters_mark = [
    (first_json_file, empty_f1),
    (empty_f1, first_json_file),
    (empty_f1, empty_f2),
]


@pytest.mark.parametrize(('ff, sf'), parameters_mark)
def test_is_empty_file(ff, sf):
    with pytest.raises(ValueError) as e:
        generate_diff(ff, sf)
        print(e)
