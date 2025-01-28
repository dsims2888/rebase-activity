def say_hello(datatype, n) -> None:
    if datatype == 'int':
        for i in range(n):
            print("hello world!")
    if datatype == 'string':
        print("Hello " + n + "!")

if __name__ == "__main__":
    say_hello('int', 3)
    say_hello('string', "Walter")
    say_hello('string', "Ruth")
    say_hello('string', "Larry")
    say_hello('string', "Helen")

