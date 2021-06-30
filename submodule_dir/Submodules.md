# how to add, if?
- `git submodule add https://github.com/author/submodule submodulef`
- this results in a git-clone into `submodulef`(can be omitted if same name is preferred)
- and makes a `.gitmodules` section (info for git clients, such as vscode git-submodule-assistant)

# issues

## adding
- remove empty submodule folders and add it as shown above
- check `.gitmodules` for duplicate entries
- have no other changes lying around (commit them first)

## git submodule assistant vscode - statusbar
- goes apeshit sometimes with 2 submodules and changes in them
- freezes on duplicate entries in `.gitmodules`