let s:plugin_path = escape(expand('<sfile>:p:h'), '/')
function! test#DrawFace()
    exe 'pyfile ' . s:plugin_path . '/../pythonx/test.py'
    python drr()
endfunction
