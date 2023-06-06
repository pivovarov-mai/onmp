ensure_path( 'TEXINPUTS', 'styles/diploma//');
$pdflatex = 'xelatex -synctex=1 -interaction=nonstopmode -shell-escape %O %S';