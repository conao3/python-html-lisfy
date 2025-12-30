# html-lisfy

A Python tool that converts HTML into S-expressions (Lisp-like syntax).

## Overview

html-lisfy parses HTML documents and transforms them into a readable S-expression format. Each HTML element becomes a list with the tag name, attributes, and children.

The output format follows this structure:
```
(tag attributes children...)
```

Where:
- `tag` - The HTML element name
- `attributes` - An alist of attributes, or `nil` if none
- `children` - Text content and nested elements

## Installation

```bash
pip install html-lisfy
```

Or with Poetry:

```bash
poetry add html-lisfy
```

## Usage

### Interactive Mode

Run the REPL for quick conversions:

```bash
html-lisfy
```

```
html-lisfy> <h1>Hello</h1>
(h1 nil Hello)

html-lisfy> <div class="container">content</div>
(div ((class . "container")) content)
```

### Examples

Simple elements:

```
<h1>Title</h1>
=> (h1 nil Title)
```

Nested elements:

```
<body><div>content</div></body>
=> (body nil (div nil content))
```

Mixed content:

```
<p>Line 1<br />Line 2</p>
=> (p nil Line 1 (br nil) Line 2)
```

Elements with attributes:

```
<div class="container" id="main">content</div>
=> (div ((class . "container") (id . "main")) content)
```

## Development

```bash
git clone https://github.com/conao3/python-html-lisfy.git
cd python-html-lisfy
poetry install
poetry run html-lisfy
```

## License

Apache-2.0
