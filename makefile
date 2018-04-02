init:
	pip install -r requirements.txt

unit:
	python -m unittest discover

unit-v:
	python -m unittest discover -v

watch-unit:
	until ack -f --python | entr -d python -m unittest discover; do sleep 1; done

watch-unit-v:
	until ack -f --python | entr -d python -m unittest discover -v; do sleep 1; done
