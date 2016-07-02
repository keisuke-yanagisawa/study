CXX=g++
CXXFLAGS=-O3
BOOST_INSTALL_PATH ?= /usr

BOOSTIP=-I$(BOOST_INSTALL_PATH)/include
BOOSTLP=-L$(BOOST_INSTALL_PATH)/lib64 -L$(BOOST_INSTALL_PATH)/lib

.SUFFIXES: .cpp .o

ALL = objs mcs

MCS_OBJS = objs/mcs.o objs/dimacs_read.o

.PHONY: clean all

all: $(ALL)

objs:
	mkdir -p objs

mcs: $(MCS_OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^ 
objs/%.o: %.cpp %.hpp
	$(CXX) $(CXXFLAGS) -o $@ -c $<

objs/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c $<

clean:
	rm -rf $(ALL)
