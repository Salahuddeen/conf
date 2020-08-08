# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# User specific aliases and functions
export GOPATH=$HOME/go
export GOBIN=$HOME/bin

# Setup Starship prompt
eval "$(starship init bash)"

#alias
alias vi="nvim"
alias yd="youtube-dl -ci --extract-audio --audio-format mp3"

#ENVAARS
export PATH=$PATH:~/bin
