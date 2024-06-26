# In English

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

# In korean

### 명령 모드

명령 모드에서의 작업은 다음과 같다:

1. 커서 이동
2. 삭제, 대체/수정
3. 복사, 붙여넣기
4. 검색, 교체
5. 파일 저장, 불러오기
6. 종료

#### 커서 이동

- `h`, `j`, `k`, `l`: `←`, `↓`, `↑`, `→`에 해당.
- `^`: 줄의 시작.
- `$`: 줄의 끝.
- `b`: 단어 단위로 뒤로 이동.
- `w`: 단어 단위로 앞으로 이동.
- `e`: 단어의 끝으로 이동.
- `^B`: 한 화면 위로 이동 (Backward).
- `^F`: 한 화면 아래로 이동 (Forward).
- `^U`: 반 화면 위로 이동 (Up).
- `^D`: 반 화면 아래로 이동 (Down).
- `:n` 또는 `nG`: n번째 줄로 이동.

명령어를 반복하려면 명령어 앞에 숫자를 입력한다.
- 예: `5h` = 왼쪽으로 5번 이동

#### 텍스트 삭제

- `x`: 한 글자 삭제.
- `X`: 왼쪽 글자 삭제.
- `dw`: 한 단어 삭제.
- `dd`: 한 줄 삭제.
- `D`: 현재 커서에서 줄의 끝까지 삭제.
- Ex 모드에서: `:range d` 또는 `:.,.+nd`.

#### 텍스트 수정

- **교체/대체**
  - `r`: 한 글자 교체.
  - `cw`: 단어 교체.
  - `cc`: 한 줄 교체.
  - `R`: 현재 커서 위치부터 연속적으로 교체.

⇒ 텍스트를 수정할 때, 삭제된 텍스트는 교체되고, 입력 모드로 전환되어 변경을 입력할 수 있다.

#### 텍스트 복사 및 붙여넣기

- `yy` 또는 `Y`: 한 줄 복사.
- `:range y`: 범위 내의 줄 복사.
- `yw`: 한 단어 복사.
- `p`: 현재 커서 뒤에 붙여넣기.
- `P`: 현재 커서 앞에 붙여넣기.
- `:pu`: 현재 커서 뒤에 붙여넣기.

#### 실행 취소 및 반복

- `u`: 가장 최근의 편집 명령 취소.
- `U`: 현재 줄에서 모든 편집 취소.
- `:e!`: 현재 변경 사항을 버리고 마지막으로 저장된 버전으로 되돌림.
- `.`: 마지막 명령 반복.
- `J`: 줄 연결.
- `^L`: 화면을 다시 그려 다른 프로그램의 불필요한 출력을 제거.

#### 검색 및 교체

- `/string[Enter]`: 앞으로 검색.
- `?string[Enter]`: 뒤로 검색.
- `/\<string\>`: 전체 단어 검색.
- `n/N`: 검색 반복 → 마지막 검색 명령 반복/방향 반대로.
- `:range s/old/new/`: 범위 내 각 줄에서 old를 new로 첫 번째 발생만 교체.
- `:range s/old/new/g`: 범위 내에서 old를 new로 모두 교체.
- `:.,.+ns/\<old\>/\<new\>/g`: 현재 줄부터 다음 n 줄까지 old 단어를 new 단어로 모두 교체.

#### 파일 저장 및 종료

- `:w`: 파일 저장.
- `:w filename`: 새 이름으로 파일 저장.
- `:range w filename`: 범위 내의 줄을 새 파일로 저장.
- `:q`: 종료 (변경 사항을 저장해야 종료 가능).
- `:q!`: 저장하지 않고 강제 종료.
- `:x`, `:wq`, `ZZ`: 저장하고 종료.
