NAME = keysmith

SOURCE = $(NAME).java
EXECUTABLE = $(NAME).class
PACKAGE = $(NAME).jar

COMPILE = javac -g -classpath jcommander/target/classes $(SOURCE)
COMPRESS = jar -vcf $(PACKAGE) $(NAME) -C jcommander/target/classes .
# RUN = java -classpath jcommander/target/classes:. keysmith


default: all

fresh: new all


all: $(EXECUTABLE)

executable: clean $(EXECUTABLE)

package: new $(PACKAGE)


clean:
	-rm $(EXECUTABLE)
	-rm *.class

new: clean
	-rm $(PACKAGE)


$(EXECUTABLE): $(SOURCE)
	$(COMPILE)

$(PACKAGE):
	$(COMPRESS)
