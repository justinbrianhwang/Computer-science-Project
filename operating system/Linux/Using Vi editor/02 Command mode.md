
### Command Mode

Operations in Command Mode are as follows:

1. Cursor movement
2. Deletion, substitution/modification
3. Copying, pasting
4. Searching, replacing
5. Saving, loading files
6. Exiting

#### Cursor Movement

- `h`, `j`, `k`, `l`: Correspond to `←`, `↓`, `↑`, `→`.
- `^`: Start of the line.
- `$`: End of the line.
- `b`: Back by word.
- `w`: Forward by word.
- `e`: End of the word.
- `^B`: One screen up (Backward).
- `^F`: One screen down (Forward).
- `^U`: Half screen up (Up).
- `^D`: Half screen down (Down).
- `:n` or `nG`: Go to line number n.

To repeat command keys, enter a number before the command.
- Example: `5h` = move left 5 times

#### Deleting Text

- `x`: Delete a character.
- `X`: Delete the character to the left.
- `dw`: Delete a word.
- `dd`: Delete a line.
- `D`: Delete from the current cursor to the end of the line.
- In Ex mode: `:range d` or `:.,.+nd`.

#### Modifying Text

- **Replace/Substitute**
  - `r`: Replace a single character.
  - `cw`: Change a word.
  - `cc`: Change a line.
  - `R`: Replace continuously from the current cursor position.

⇒ When modifying text, the deleted text is replaced, and you enter Insert Mode to make changes.

#### Copying and Pasting Text

- `yy` or `Y`: Copy a line.
- `:range y`: Copy a range of lines.
- `yw`: Copy a word.
- `p`: Paste after the current cursor.
- `P`: Paste before the current cursor.
- `:pu`: Paste after the current cursor.

#### Undo and Repeat

- `u`: Undo the most recent edit command.
- `U`: Undo all edits on the current line.
- `:e!`: Discard current changes and revert to the last saved version of the file.
- `.`: Repeat the last command.
- `J`: Join lines.
- `^L`: Redraw the screen to remove any extraneous output from other programs.

#### Searching and Replacing

- `/string[Enter]`: Search forward.
- `?string[Enter]`: Search backward.
- `/\<string\>`: Search for the whole word.
- `n/N`: Repeat search → Repeat the last search command/reverse direction.
- `:range s/old/new/`: Replace the first occurrence of old with new in each line of the range.
- `:range s/old/new/g`: Replace all occurrences of old with new in the range.
- `:.,.+ns/\<old\>/\<new\>/g`: Replace all occurrences of the word old with new from the current line to the next n lines.

#### Saving and Exiting Files

- `:w`: Save the file.
- `:w filename`: Save the file with a new name.
- `:range w filename`: Save a range of lines to a new file.
- `:q`: Quit (must save changes to quit).
- `:q!`: Force quit without saving.
- `:x`, `:wq`, `ZZ`: Save and exit.
