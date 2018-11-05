# hanoi
Tkinter interface for Hanoi Tower which also accept terminal commands 

**API**

Hanoi(n)
  Crate an interface for a Hanoi Tower with n disks.

.mainloop()
  tkinter root mainloop to keep window open

.destroy()
  tkinter destroy method to close widget

.mudar(i, j)
  Hanoi method to move a disk from i tower to j tower, where i and j must be an integer between 0 and 2: i, j = 0, 1, 2

.solve(time_sleep)
  Hanoi object method to solve the Hanoi Tower through a recursive algorithm, with a time_sleep, in seconds, between each move. 

example:


>> from hanoi import Hanoi

>> hanoi = Hanoi(4)

>> hanoi.mudar(0, 1)

>> hanoi = Hanoi(5)

>> hanoi.solve(0.1)

>> hanoi.destroy()
