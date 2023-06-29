# python-html-lisfy

## Usage

```bash
$ poetry install
$ poetry run html-lisfy
```

## Example

```html
$ poetry run html-lisfy
html-lisfy> <h1>asdf</h1>
(h1 nil asdf)

html-lisfy> <body><div>asdf</div></body>
(body nil (div nil asdf))

html-lisfy> <p>1111<br />2222</p>
(p nil 1111 (br nil) 2222)

html-lisfy> <div class="container">asdf</div>
(div ((class . "container")) asdf)
```
