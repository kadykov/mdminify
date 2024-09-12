from mdminify import mdminify


# Test removing a single markdown link
def test_remove_single_link():
    markdown_text = "I am proficient in [Python](https://www.python.org/)."
    expected_plain_text = "I am proficient in Python."
    expected_links = {"Python": "https://www.python.org/"}

    plain_text, links = mdminify.remove_links(markdown_text)

    assert plain_text == expected_plain_text, "Plain text did not match expected output"
    assert links == expected_links, "Links dictionary did not match expected output"


# Test removing multiple markdown links
def test_remove_multiple_links():
    markdown_text = "I am proficient in [Python](https://www.python.org/) and [JavaScript](https://www.javascript.com/)."
    expected_plain_text = "I am proficient in Python and JavaScript."
    expected_links = {
        "Python": "https://www.python.org/",
        "JavaScript": "https://www.javascript.com/",
    }

    plain_text, links = mdminify.remove_links(markdown_text)

    assert (
        plain_text == expected_plain_text
    ), "Plain text did not match expected output for multiple links"
    assert (
        links == expected_links
    ), "Links dictionary did not match expected output for multiple links"


# Test reinserting a single markdown link
def test_reinsert_single_link():
    plain_text = "I am proficient in Python."
    links = {"Python": "https://www.python.org/"}
    expected_restored_text = "I am proficient in [Python](https://www.python.org/)."

    restored_text = mdminify.reinsert_links(plain_text, links)

    assert (
        restored_text == expected_restored_text
    ), "Restored text did not match expected output for single link"


# Test reinserting multiple markdown links
def test_reinsert_multiple_links():
    plain_text = "I am proficient in Python and JavaScript."
    links = {
        "Python": "https://www.python.org/",
        "JavaScript": "https://www.javascript.com/",
    }
    expected_restored_text = "I am proficient in [Python](https://www.python.org/) and [JavaScript](https://www.javascript.com/)."

    restored_text = mdminify.reinsert_links(plain_text, links)

    assert (
        restored_text == expected_restored_text
    ), "Restored text did not match expected output for multiple links"


# Test plain text with no markdown links
def test_no_links():
    plain_text = "I am proficient in Python and JavaScript."
    links = {}
    expected_restored_text = plain_text  # No changes expected

    restored_text = mdminify.reinsert_links(plain_text, links)

    assert (
        restored_text == expected_restored_text
    ), "Text with no links should remain unchanged"
