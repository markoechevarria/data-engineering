# 26. Top-Down design

* As programs get larger and more complex, they become more difficult to design, code, and maintain. As with any large project, it is often a good idea to break large, complex tasks into a series of small, simple tasks.

## Shell functions

* We could write three separate scripts and place them in a directory listed in our PATH, or we could embed the scripts within our program as shell functions

```
function name {
    commands
    return
}
```

* Global variables maintain their existence throughout the program.
* Local variables are accesible only within the shell function in which they are defined
