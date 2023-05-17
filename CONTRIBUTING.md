# Contributing to cgpt 🚀

First off, thank you for considering contributing to cgpt. It's people like you that make cgpt such a great tool. 

## Where do I go from here?

If you've noticed a bug or have a feature request, make one! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

## Fork & Create a Branch

If this is something you think you can fix or feature you can implement, then follow these steps:

1. [Fork cgpt](https://help.github.com/articles/fork-a-repo) and create a branch with a descriptive name.
2. A good branch name would be (where issue #325 is the ticket you're working on): `325-contribution-format`

## Get Coding!

- Make sure your code meets our [Style Guide](#style-guide).
- Make sure your code is properly commented and documented.
- Include tests that cover any code changes you make.
- Make sure the test suite passes before you commit your changes.
- If the changes apply to a specific issue or proposal, reference it in the commit messages. For example `resolves #325`.

## Submitting a Pull Request

Submit a [pull request](https://help.github.com/articles/about-pull-requests/) 🎉

## Style Guide

We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code. In addition, we follow these rules:

### Code Layout

1. Indentation: 4 spaces, no tabs
2. Maximum line length: 79 characters for code, 72 for comments and docstrings
3. Blank lines: Surround top-level function and class definitions with two blank lines. Method definitions inside a class are surrounded by a single blank line.

### Imports

1. Imports should be grouped in the following order:
    - Standard library imports
    - Related third party imports
    - Local application/library specific imports
2. You should put a blank line between each group of imports.

### White Space

1. Immediately before the open parenthesis that starts the argument list of a function call
2. Immediately before the open parenthesis that starts an indexing or slicing
3. More than one space around an assignment (or other) operator to align it with another.

### Comments

1. Comments should be complete sentences. If a comment is a phrase or sentence, its first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).
2. If a comment is short, the period at the end can be omitted. Block comments generally consist of one or more paragraphs built out of complete sentences, and each sentence should end in a period.
3. You should use two spaces after a sentence-ending period.

### Naming Conventions

1. Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
2. Avoid using names that are too general or too wordy. Strike a good balance between the two.
3. Bad: data_structure, my_list, info_map, dictionary_for_the_purpose_of_storing_data_representing_word_definitions
4. Good: user_profile, menu_options, word_definitions
5. Don’t be a jackass and name things “O”, “l”, or “I”

When in doubt, refer to PEP 8 or the existing CGPT codebase. Happy coding! 🎉

## Code of Conduct

By participating in this project, you agree to abide by [our code of conduct](CODE_OF_CONDUCT.md).

## Questions?

If you have any questions, create an [issue](https://github.com/andresvillenas/cgpt/issues) or contact us directly. 
