NAME = keysmith

SOURCE = $(NAME).c
EXECUTABLE = $(NAME).out
PACKAGE = $(NAME).tgz

COMPILE = gcc -std=c99 -pedantic -Wall -lcurl -o $(EXECUTABLE) $(SOURCE)
COMPRESS = tar -vzcf $(PACKAGE) *


default: all

fresh: new all


all: $(EXECUTABLE)

executable: clean $(EXECUTABLE)

package: new $(PACKAGE)


clean:
	-rm $(EXECUTABLE)
	-rm *.o

new: clean
	-rm $(PACKAGE)


$(EXECUTABLE): $(SOURCE)
	$(COMPILE)

$(PACKAGE):
	$(COMPRESS)
