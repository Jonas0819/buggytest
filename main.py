#!/usr/bin/python3
from snippets import (
    lambda_array,
    read_file,
    calculate_unpaid_loans,
    calculate_paid_loans,
    average_paid_loans,
    foo
)

if __name__ == "__main__":
    try:
        lambdas = lambda_array()
        json_file = read_file()
        print(json_file)
        print(lambdas[0](10))
        print(calculate_unpaid_loans(json_file))
        print(calculate_paid_loans(json_file))
        print(average_paid_loans(json_file))
        assert (lambdas[0](10) == 19), "lambdas[0](10) should equal 19"
        assert (len(json_file.get("loans")) == 15), "Number of loans should equal 15"
        assert (calculate_unpaid_loans(json_file) == 11062), "Total unpaid loans should equal 11062"
        assert (calculate_paid_loans(json_file) == 29493.85304), "Total paid loans should equal 29493.85304"
        assert (average_paid_loans(json_file) == 2681.2593672727276), "Average of paid loans should equal 2681.2593672727276"
        assert (foo() == ["baz"]), "This should return a single item 'bazx'"
        assert (foo() == ["baz"]), "When I call the function the second time I should still get a single element in the array"
        print("All test passed successfullw awyx!! Pepitos 😀")
    except (
        AssertionError, SyntaxError, TypeError
    ) as error:
        print(error, " 😢")

