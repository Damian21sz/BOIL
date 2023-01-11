run:
	python3 main.py

test:
	python3 -m pytest test_gui.py

clean:
	rm -rf __pycache__
