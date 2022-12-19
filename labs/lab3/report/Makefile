FILES = $(patsubst %.md, %.docx, $(wildcard *.md))
FILES += $(patsubst %.md, %.pdf, $(wildcard *.md))

FILTERS =
OPTIONS =
PDF_ENGINE =
PDF_OPTIONS =
FORMAT_OPTIONS =

FILTERS += -F pandoc-crossref
PDF_ENGINE += --pdf-engine=lualatex --pdf-engine-opt=--shell-escape
OPTIONS += --number-sections
BIB_OPTIONS = --citeproc


%.docx: %.md
	-pandoc "$<" -o "$@"

%.pdf: %.md
	-pandoc "$<" $(PDF_ENGINE)) -o "$@"

all: $(FILES)


clean:
	-rm $(FILES) *~

cleanall: clean