if !has('python')
    echo "test.vim ERROR: Required vim compiled with +python"
    finish
endif
""exe 'pyfile ../autoload/test.py'
nnoremap <leader>o :call test#DrawFace()<CR>
