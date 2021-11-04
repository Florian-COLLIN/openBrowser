# openBrowser
openBrowsser is a Sublime Text plug-in, which allows you to add a keyboard shortcut, to directly access a website from a selection.

# Install packages
...

# Install key
In Sublime Text, you go to `Preferences > Key Bindings`, and on the right you add :
```JSON
{
        "keys" : ["ctrl+alt+g"],
        "command": "open_browser",
        "args": {
            "url": "https://docs.python.org/library/%s"
        }
    },
```
`ctral+alt+g` and `https://docs.python.org/library/%s` are examples, you can replace them.

- %s : the selection

# Use
Now, if you select a text, a word... and that you do (with the example above) 'ctrl+alt+g', you will be redirected to the page https://docs.python.org/library/ plus the selection.
