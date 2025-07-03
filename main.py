import pathlib

from cats.cats import get_cats_info
from salary import total_salary
from vcd import dirtree

total_salary('data/salary.csv')
get_cats_info('data/cats.csv')
dirtree(pathlib.Path(pathlib.Path.cwd()))

