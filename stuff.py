class Foo:

    def foo(self):
        print("foo")


class Bar:

    def bar(self):
        print("bar")

    # ::> owners hwkns
    def reference_foo(self):
        f = Foo()
        f.foo()
