


TARGET ?= daclient

CFLAGS=-g -Wall -lm

$(TARGET): $(TARGET).o paths.h
	$(CC) $(TARGET).o -o $@ $(LDFLAGS)
	chmod 6755 $(TARGET)

paths.h:
	bash ./create_paths_h.sh

.PHONY: clean run valgrind

clean:
	$(RM)  *.o
	$(RM) $(TARGET)

run: $(TARGET)
	@./$(TARGET)

valgrind: $(TARGET)
	valgrind --leak-check=full ./$(TARGET)


