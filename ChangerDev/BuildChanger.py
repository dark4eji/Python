import version_selection as vs
import config_selection as cs
import folder_selector as fs

w_a = 'Некорректный ответ, попробуйте снова'

while True:

    sel = vs.version_selection(w_a)

    if sel is None:
        print(True)
    else:
        global deq
        deq = cs.config_selection(sel, w_a)

    if deq is None:
        print(True)
    else:
        global fel
        fel = fs.folder_finder(deq)



