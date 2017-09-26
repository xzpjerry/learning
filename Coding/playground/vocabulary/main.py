#!/usr/bin/env python3
#!/usr/bin/python3
#!/usr/bin/env python3

import gui
import matching

basic = gui.tk.Tk()
basic.maxsize(1920, 1080)
basic.title('SRT dictionary')
app = gui.Application(func=matching.matching, master=basic)
basic.mainloop()
