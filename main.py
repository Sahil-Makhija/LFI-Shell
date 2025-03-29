from cmd_loop import Term

term = Term()
try:
    term.cmdloop()
except KeyboardInterrupt:
    print()