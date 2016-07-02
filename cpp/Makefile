CXX=g++
CXXFLAGS=
BOOST_INSTALL_PATH ?= /usr

BOOSTIP=-I$(BOOST_INSTALL_PATH)/include
BOOSTLP=-L$(BOOST_INSTALL_PATH)/lib64 -L$(BOOST_INSTALL_PATH)/lib

.SUFFIXES: .cpp .o

ALL = objs mcs

MCS_OBJS = objs/mcs.o

.PHONY: clean all

all: $(ALL)

objs:
	mkdir -p objs

mcs: $(MCS_OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^ 
objs/mcs.o: mcs.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c $<

clean:
	rm -rf $(ALL)
