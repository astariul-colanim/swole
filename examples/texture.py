from swole import Application
from swole.widgets import Input, Button, Markdown, Header


Input()
Input(wide=False)
Input(placeholder="placeholder", wide=False)
Input(label="labeled", placeholder="placeholder", wide=False)

Button("Button")
Button("Button", wide=True)
Button("Button", primary=True)
Button("Button", primary=True, wide=True)

Markdown("Short Markdown")
Markdown("Super Super Super Super Super Super Super Super Super Super Super Super Super Super Super Super Super "
         "Super Super Long Markdown")

Header(level=1)
Header()
Header(level=3)
Header(level=4)
Header(level=5)
Header(level=6)
Header(level=1, center=True)
Header(center=True)
Header(level=3, center=True)
Header(level=4, center=True)
Header(level=5, center=True)
Header(level=6, center=True)

Markdown("""# Title 1
## Title 2

Markdown.
Markdown.

This is a list :
* Element 1
* Element 2

Normal text
**Bold text**
*Italic text*
_Italic text_

---

Horizontal ruler.

Code `inside` the line.

```python
Full code
```""")


if __name__ == "__main__":
    Application().serve()
