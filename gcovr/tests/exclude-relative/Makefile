CFLAGS= -fprofile-arcs -ftest-coverage -fPIC

all:
	$(CXX) $(CFLAGS) -c file1.cpp -o file1.o
	$(CXX) $(CFLAGS) -c main.cpp -o main.o
	$(CXX) $(CFLAGS) main.o file1.o -o testcase

run: txt xml html sonarqube coveralls

coverage.json:
	./testcase
	# use a relative filter here
	# if testcase.exe exists (windows) use wrong case to check caseinsensitive filter
	$(GCOVR) -e '$(if $(wildcard ./testcase.exe),File1.cpp,file1.cpp)'  --json $@

txt: coverage.json
	$(GCOVR) -a $< -o coverage.txt

xml: coverage.json
	$(GCOVR) -a $< -x -o coverage.xml

html: coverage.json
	$(GCOVR) -a $< --html-details -o coverage.html

sonarqube: coverage.json
	$(GCOVR) -a $< --sonarqube sonarqube.xml

coveralls: coverage.json
	$(GCOVR) -a $< --coveralls coveralls.json

clean:
	rm -f testcase
	rm -f *.gc* *.o
	rm -f coverage*.* sonarqube*.* coveralls.json
