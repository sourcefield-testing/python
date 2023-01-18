class Foo:

    def foo(self):
        print("foo")


class Bar:

    def bar(self):
        testing = (1,)
        if testing:
            bar = [
                "a",
                "b",
                "c",
            ]
            print("testing")
        print("bar")

    # ::> owners hwkns
    def reference_foo(self):
        f = Foo()
        f.foo()
