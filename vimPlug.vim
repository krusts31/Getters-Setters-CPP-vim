let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'vimPlug/python'))
sys.path.insert(0, python_root_dir)
import sample
EOF

function! InsertClass(arg, x)
python3 << EOF
import vim
import sample
sample.insert_class(vim.eval("a:arg"), vim.eval("a:x"))
EOF
endfunction
command! -nargs=+ InsertClass call InsertClass(<f-args>)

function! DeffineClass(arg, x)
python3 << EOF
import vim
import sample
sample.deffine_class(vim.eval("a:arg"), vim.eval("a:x"))
EOF
endfunction
command! -nargs=+ DeffineClass call DeffineClass(<f-args>)

function! InsertGetSet(clas, var, typ, x)
python3 << EOF
import vim
import sample
sample.insert_set_get(vim.eval("a:clas"), vim.eval("a:var"), vim.eval("a:typ"), vim.eval("a:x"))
EOF
endfunction
command! -nargs=+ InsertGetSet call InsertGetSet(<f-args>)

function! DeffineGetSet(clas, var, typ, x)
python3 << EOF
import vim
import sample
sample.deffine_set_get(vim.eval("a:clas"), vim.eval("a:var"), vim.eval("a:typ"), vim.eval("a:x"))
EOF
endfunction
command! -nargs=+ DeffineGetSet call DeffineGetSet(<f-args>)

