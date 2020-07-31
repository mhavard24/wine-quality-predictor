import click
from wqp import __version__

@click.group(name='wqp', help='A command line tool to train a wine quality predictor')
@click.version_option(__version__)
def wqp():
    pass
