up:
	@docker-compose -f docker-compose.yml up --build

destroy:
	@docker-compose -f docker-compose.yml down -v

migrations:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web python manage.py makemigrations; \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web python manage.py makemigrations; \
	fi

migrate:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web python manage.py migrate; \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web python manage.py migrate; \
	fi

test:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web pytest; \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web pytest; \
	fi

test_specific_file:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web pytest $(path); \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web pytest $(path); \
	fi
	
isort:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web isort . --profile black --skip env; \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web isort . --profile black --skip env; \
	fi

flake:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web flake8; \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web flake8; \
	fi

black:
	@docker-compose -f docker-compose.yml ps | grep "web" | grep "Up" > /dev/null; \
	if [ $$? -eq 0 ]; then \
		docker-compose -f docker-compose.yml exec web black . --exclude env; \
	else \
		docker-compose -f docker-compose.yml up --build -d && \
		docker-compose -f docker-compose.yml exec web black . --exclude env; \
	fi
