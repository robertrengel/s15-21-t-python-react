bar = 
foo = $(bar)

all:
ifdef foo
	@echo "foo is defined"
endif
ifndef bar
	@echo "but bar is not"
endif

run:
	pip install --upgrade pip && \
	python manage.py runserver 

mig:
	python manage.py makemigrations && \
	python manage.py migrate

delmig:
	rm -rf ./medical_history/migrations/00*.py
	rm -rf ./medics_profile/migrations/00*.py
	rm -rf ./api/migrations/00*.py
	rm -rf ./catalogs/migrations/00*.py

