DABUZZ_DIR = /dabuzz
DABUZZ_SERVER = stonelinks.org
DABUZZ_USER = rcos-dabuzz

deploy.remote:
	@rsync -ahvve ssh --delete --exclude-from=.rsync-ignore ./ $(DABUZZ_USER)@$(DABUZZ_SERVER):$(DABUZZ_DIR)/server
	@ssh $(DABUZZ_USER)@$(DABUZZ_SERVER) 'sudo /etc/init.d/apache2 restart && \
	                                      cd $(DABUZZ_DIR)/server && \
	                                      $(MAKE) echo.deployed '

echo.deployed:
	@echo "\n"
	@echo "======================================"
	@echo "=   server deployed to remote!       ="
	@echo "======================================"
	@echo "\n\n"

run.local:
	@python server.py
