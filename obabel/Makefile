
CXX=g++
CXXFLAGS=-O2
OBABEL=$(HOME)/.local/openbabel
.PHONY: all clean

all: modify_mol

modify_mol: modify_mol.o
	$(CXX) $(CXXFLAGS) -o $@ $< -L$(OBABEL)/lib -lopenbabel

modify_mol.o: modify_mol.cc
	$(CXX) $(CXXFLAGS) -I$(OBABEL)/include/openbabel-2.0 -o $@ -c $<

clean:
	rm -f modify_mol modify_mol.o
