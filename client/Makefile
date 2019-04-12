


TARGET ?= daclient

CFLAGS=-g -Wall -lm

$(TARGET): $(TARGET).o
	$(CC) $(TARGET).o -o $@ $(LDFLAGS)
	chmod 6755 $(TARGET)

daclient.o: daclient.c paths.h

paths.h:
	bash ./create_paths_h.sh

.PHONY: clean run valgrind

clean:
	$(RM)  *.o
	$(RM) $(TARGET)
	$(RM) paths.h

run: $(TARGET)
	@./$(TARGET)

valgrind: $(TARGET)
	valgrind --leak-check=full ./$(TARGET)


