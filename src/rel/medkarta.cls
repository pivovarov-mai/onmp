%\NeedsTexFormat{LaTeX2e}
\ProvidesClass{medkarta}[2020/09/19 Medicine card class]

\DeclareOption{a4paper}{
    \PassOptionsToClass{\CurrentOption}{article}
}

\DeclareOption{12pt}{
    \PassOptionsToClass{\CurrentOption}{article}
}

\ExecuteOptions{12pt,a4paper}
\ProcessOptions\relax

\LoadClass{article}

\sloppy

\RequirePackage[T2A]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage[russian,english]{babel}

\RequirePackage[left=1.7cm, top=2cm, bottom=1.5cm, right=1.2cm]{geometry}
\RequirePackage[normalem]{ulem}
\RequirePackage{relsize}

\RequirePackage{formular}
\setFRMinlinestyle
\setFRMbaselineskip{10pt}
%\setFRMfontencoding{\encodingdefault}
%\setFRMdfontencoding{\encodingdefault}
\setFRMfontencoding{T2A}
\setFRMdfontencoding{T2A}
\setFRMfontfamily{\ttdefault}
\setFRMdfontfamily{\sfdefault}
\newFRMenvironment{zhaloby}{\textbf{ЖАЛОБЫ}}{6}
\newFRMenvironment{anamnez}{\textbf{АНАМНЕЗ} (в т.ч.-эпид., аллерг., гинекол по показаниям)}{6}
\newFRMenvironment{status}{Status localis}{4}
\newFRMenvironment{data}{\textbf{Данные инструментальных исследований (ЭКГ, глюкометрия, пульсоксиметрия и пр.)}}{8}
\newFRMenvironment{help}{\textbf{Оказанная помощь и ее эффект (в т.ч. результаты инстр. иссл. в динамике)}}{6}
\newFRMenvironment{recomend}{\textbf{Рекомендации:}}{1}
\newFRMenvironment{signal}{\textbf{Сигнальная карта:}}{1}
\newFRMfield{count1}{0.5cm}
\newFRMfield{count2}{1cm}
\newFRMfield{count3}{1.5cm}

\RequirePackage{ifthen}
\newcommand{\underlinetext}[2]{%
\ifthenelse{\equal{#1}{#2}}{\underline{#2}}{#2}%
}
% 
%\RequirePackage{substr}
%\newcommand{\underlinetext}[2]{%
%\IfSubStringInString{#2}{#1}{\underline{#2}}{#2}%
%}

\RequirePackage{etoolbox}
\newcounter{cnt}
\newcommand\addtext[1]{%
  \stepcounter{cnt}%
  \csdef{text\thecnt}{#1}%
}
\newcommand\gettext[1]{%
  \csuse{text#1}%
}

\setlength\parindent{0pt}
\pagestyle{empty}

\endinput
