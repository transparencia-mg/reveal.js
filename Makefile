container: ## Start Docker Container
	@echo 'Starting Docker Container...'
	docker run -it --rm -p 8000:8000 \
	-v /$(PWD)/presentations:/reveal.js/presentations \
	-v /$(PWD)/dist:/reveal.js/dist \
	-v $(PWD)/index.html:/reveal.js/index.html \
	-v $(PWD)/media:/reveal.js/media \
	-v $(PWD)/css:/reveal.js/css \
	-v $(PWD)/plugin:/reveal.js/plugin nbrown/revealjs

index: 
	@echo 'Atualizando index...'
	@python scripts/generate_index.py

presentation:
	@echo 'Criando apresentação...'
	@python scripts/generate_presentation.py $(NAME)