#!/usr/bin/python3

from snippets import io,loop,foobar

if __name__ == "__main__":
    try:
        lambdas = loop.lambda_array()
        json_file = io.read_file()
        print(json_file)
        print(lambdas[0](10))
        print(io.calculate_unpaid_loans(json_file))
        print(io.calculate_paid_loans(json_file))
        print(io.average_paid_loans(json_file))
        assert (lambdas[0](10) == 19), "lambdas[0](10) should equal 19"
        assert (len(json_file.get("loans")) == 15), "Number of loans should equal 15"
        assert (io.calculate_unpaid_loans(json_file) == 11062), "Total unpaid loans should equal 11062"
        assert (io.calculate_paid_loans(json_file) == 29493.85304), "Total paid loans should equal 29493.85304"
        assert (io.average_paid_loans(json_file) == 2681.2593672727276), "Average of paid loans should equal 2681.2593672727276"
        assert (foobar.foo() == ["baz"]), "This should return a single item 'baz'"
        assert (foobar.foo() == ["baz"]), "When I call the function the second time I should still get a single element in the array"
        print("All test passed successfully!! 😀")
    except (
        AssertionError, SyntaxError, TypeError
    ) as error:
        print(error, " 😢")


