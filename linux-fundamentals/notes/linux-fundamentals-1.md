# Linux Fundamentals - Part 1 🐧

## 📅 Date: July 22, 2025

## 🔍 What I Learned Today:
- What Linux is and why it is important in cybersecurity
- Using the TryHackMe virtual machine
- Basic terminal commands

## 🧪 Commands Practiced:

| Command | Description |
|--------|-------------|
| `pwd` | Shows current directory |
| `ls` | Lists files in directory |
| `cat` | Concatenate |
| `pwd` | print working directory |
| `cd` | Changes directory |
| `mkdir` | Creates a new folder |
| `touch` | Creates a new file |

## Operators:
| Operator | Description |
|--------|-------------|
| `&` | Runs a command in the background |
| `&&` | Chains commands, runs the next only if the first succeeds |
| `>` | Redirects output, replaces content in the target file |
| `>>` | Appends output to the file without overwriting existing content |

## 🧠 Notes:
- Linux is a surprisingly widespread operating system that powers many everyday technologies you likely use daily, from the websites you visit to in-car systems and retail checkouts.
- The first version of the Linux kernel, version 0.01, was released by Linus Torvalds on September 17, 1991.
- The echo command is used to output any text you provide, while the whoami command identifies the user you are currently logged in as.
- I have learned how to use essential Linux commands like cd, ls, cat, and pwd to navigate the file system and view file contents.
- Use find -name filename to search for specific files in your current directory and subfolders.
You can also use wildcards like find -name "*.txt" to list all .txt files.
- Use grep "text" filename to search inside files for specific words or values.
Helpful for quickly filtering large files like logs or configs.
- `ls -la` shows hidden files and more details
- Linux is case-sensitive! `File.txt` and `file.txt` are different
- I used `clear` to clean my terminal view

## 🚩 Flags Found:
- Task 3 Flag: `THM{basic-linux-command}` ✅

## 🪜 Challenges:
- I forgot how to use `cd ..` to go back. Took me a few tries!
- Took time to understand absolute vs relative paths

## 💬 Reflections:
This was a great start. I feel more confident using the Linux terminal. Going to try and memorize at least 10 commands from today!

---

