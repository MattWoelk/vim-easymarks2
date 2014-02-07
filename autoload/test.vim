let s:plugin_path = escape(expand('<sfile>:p:h'), '/')
function! test#DrawFace()
    exe 'pyfile ' . s:plugin_path . '/test.py'
    python drr()
endfunction
