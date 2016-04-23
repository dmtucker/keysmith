NAME = keysmith

SOURCE = $(NAME).hs
EXECUTABLE = $(NAME)
PACKAGE = $(NAME).tgz

COMPILE = ghc -v -o $(EXECUTABLE) $(SOURCE)
COMPRESS = tar -vzcf $(PACKAGE) *


default: all

fresh: new all


all: $(EXECUTABLE)

executable: clean $(EXECUTABLE)

package: new $(PACKAGE)


clean:
	-rm $(EXECUTABLE)
	-rm *.hi
	-rm *.o

new: clean
	-rm $(PACKAGE)


$(EXECUTABLE): $(SOURCE)
	$(COMPILE)

$(PACKAGE):
	$(COMPRESS)
