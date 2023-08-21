call plug#begin()
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/nerdtree'
Plug 'leafgarland/typescript-vim'
Plug 'peitalin/vim-jsx-typescript'
Plug 'chrisbra/vim-autosave'
call plug#end()

syntax on
filetype indent on

set autoindent
set expandtab
set hlsearch
set ignorecase
set incsearch
set paste
set scrolloff=4
set shiftwidth=4
set showcmd
set showmatch
set softtabstop=4
set tabstop=4
set ttyfast
set undodir=$HOME/.vim/undo
set undofile
set wildmenu
set wildmode=longest,list

" Exit insertion mode
imap jk <Esc>

" Airline
let g:airline_theme='deus'
let g:airline_powerline_fonts = 1

" No background for vertical fill char
highlight VertSplit cterm=NONE

