function! test#DrawFace()
    let s:plugin_path = escape(expand('<sfile>:p:h'), '/')
    exe 'pyfile ' . s:plugin_path . '/test.py'
    python drr()
endfunction
