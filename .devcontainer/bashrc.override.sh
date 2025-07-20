# set some django env vars
source /entrypoint

# restore default shell options
set +o errexit
set +o pipefail
set +o nounset

# start ssh-agent
# https://code.visualstudio.com/docs/remote/troubleshooting
eval "$(ssh-agent -s)"

# aliases
alias tw="tailwindcss -i /workspaces/assets/css/tw-input.css -o /workspaces/app/static/css/ledgerko-ui.css"
alias tw-watch="tw --watch"
alias tw-build="tw --minify"