import click
import os
from click.testing import CliRunner
from bagtoingest import cli


def test_returns_error_if_path_does_not_exist():
    runner = CliRunner()
    result = runner.invoke(cli, "foo")
    assert result.exit_code == 2


def test_returns_error_if_no_bag_found():
    runner = CliRunner()
    result = runner.invoke(cli, "./tests/test_files/no_bag/")
    assert result.exit_code == 1


def test_exits_if_bag_found():
    runner = CliRunner()
    result = runner.invoke(cli, "./tests/test_files/one_bag/")
    assert result.exit_code == 0


def test_write_file_to_destination():
    runner = CliRunner()
    outfile = ("./tests/bagout.tsv")
    result = runner.invoke(cli, ["./tests/test_files/one_bag/", "--destination", "./tests/"])
    assert os.path.exists(outfile) == True
    os.remove(outfile)


def test_output_is_expected_output():
    runner = CliRunner()
    outfile = ("./tests/bagout.tsv")
    result = runner.invoke(cli, ["./tests/test_files/one_bag/", "--destination", "./tests/"])
    f = open(outfile)

    ## line count
    expected_lines = 2
    actual_lines = sum(1 for line in f)
    assert expected_lines == actual_lines

    ## column count
    expected_columns =  18 + 6*4
    for line in f:
        actual_columns = len(("\t").split(line)) 
        assert expected_columns == actual_columns
