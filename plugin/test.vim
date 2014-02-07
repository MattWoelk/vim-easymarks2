if !has('python')
    echo "test.vim ERROR: Required vim compiled with +python"
    finish
endif

nnoremap <leader>o :call test#DrawFace()<CR>
