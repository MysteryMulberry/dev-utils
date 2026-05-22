APP ?= myapp

.PHONY: build test lint run clean

build:
	go build -o bin/$(APP) ./cmd/$(APP)

test:
	go test -v -cover ./...

lint:
	golangci-lint run

run: build
	./bin/$(APP)

clean:
	rm -rf bin/
