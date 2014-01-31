if !has('python')
    echo "vim-python-test-plugin ERROR: Required vim compiled with +python"
    finish
endif

function! Reddit()
python << EOF
import vim, urllib2
import json

TIMEOUT = 20
URL = "http://reddit.com/.json"

try:
    response = urllib2.urlopen(URL, None, TIMEOUT).read()
    json_response = json.loads(response)

    posts = json_response.get("data", "").get("children", "")

    # each line is a list in this buffer.
    # we delete them all
    del vim.current.buffer[:]

    # append some nice lines
    vim.current.buffer[0] = 80*"-"

    for post in posts:
        post_data = post.get("data", {})
        up = post_data.get("ups", 0)
        down = post_data.get("downs", 0)
        title = post_data.get("title", "NO TITLE").encode("utf-8")
        url = post_data.get("url").encode("utf-8")

        vim.current.buffer.append("    %s [%s]"%(title, url,))
        vim.current.buffer[0] = 80*"-"
except Exception, e:
    print e

EOF
endfunction

command! -nargs=0 Reddit call Reddit()
