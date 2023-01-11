run:
	python main.py

test:
	python -m pytest test_gui.py

clean:
	rm -rf __pycache__