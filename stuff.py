class Foo:

    def foo(self):
        print("foo")


class Bar:

    def bar(self):
        testing = True
        if testing:
            bar = ["a", "b", "c"]
        print("testing")
        print("bar")

    # ::> owners hwkns
    def reference_foo(self):
        f = Foo()
        f.foo()
