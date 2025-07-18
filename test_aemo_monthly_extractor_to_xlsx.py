import os
import shutil
import pytest
from aemo_monthly_extractor_to_xlsx import app, recreate

def test_valid_app():
	'''
	Validation test for the app function
	'''
	try:
		app()
		for obj in ['result', 'result/result.xlsx']:
			if not os.path.exists(obj):
				pytest.fail(f'No Output Data')
		shutil.rmtree('result')
	except Exception as e:
		pytest.fail(f'The program is invalid. Error: {e}')

def test_valid_recreate():
	'''
	Validation test for the recreate function
	'''
	try:
		path: str = 'test_dir'
		recreate(path)
		if os.path.exists(path):
			shutil.rmtree(path)
		else:
			pytest.fail(f'The directory is absent.')
	except Exception as e:
		pytest.fail(f'The program is invalid. Error: {e}')