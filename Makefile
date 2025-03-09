install:
	python3 -m venv .env
#source .env/bin/activate

RED=\033[1;31m
GREEN=\033[1;32m
YELLOW=\033[1;33m
BLUE=\033[1;34m
RESET=\033[0m

check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		printf "$(RED)❌ No virtual environment detected!$(RESET)\n"; \
		printf "$(YELLOW)⚠️ Run: source .env/bin/activate$(RESET)\n"; \
		exit 1; \
	else \
		printf "$(GREEN)✅ Virtual env is active: $$VIRTUAL_ENV$(RESET)\n"; \
	fi

#norminette=flake8