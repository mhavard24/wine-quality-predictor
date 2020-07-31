import click
from wqp import __version__

@click.group(name='wqp', help='A command line tool to train a wine quality predictor')
@click.version_option(__version__)
def wqp():
    pass


	
	
@wqp.group(name='jobs')
def jobs():
    pass
@jobs.command()
@click.option('--data','-d',  help='given data path')
def train(data):
	import wqp.workflow as wf
	wf.model_training_workflow(data) 

