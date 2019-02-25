L1, l1 = '\u0410', '\u0430'
L2, l2 = '\u0411', '\u0431'
L3, l3 = '\u0412', '\u0432'
L4, l4 = '\u0413', '\u0433'
L5, l5 = '\u0414', '\u0434'
L6, l6 = '\u0415', '\u0435'
L7, l7 = '\u0416', '\u0436'
L8, l8 = '\u0417', '\u0437'
L9, l9 = '\u0418', '\u0438'
L10, l10 = '\u0419', '\u0439'
L11, l11 = '\u041A', '\u043A'
L12, l12 = '\u041B', '\u043B'
L13, l13 = '\u041C', '\u043C'
L14, l14 = '\u041D', '\u043D'
L15, l15 = '\u041E', '\u043E'
L16, l16 = '\u041F', '\u043F'
L17, l17 = '\u0420', '\u0440'
L18, l18 = '\u0421', '\u0441'
L19, l19 = '\u0422', '\u0442'
L20, l20 = '\u0423', '\u0443'
L21, l21 = '\u0424', '\u0444'
L22, l22 = '\u0425', '\u0445'
L23, l23 = '\u0426', '\u0446'
L24, l24 = '\u0427', '\u0447'
L25, l25 = '\u0429', '\u0449'
L26, l26 = '\u042A', '\u044A'
L27, l27 = '\u042C', '\u044C'
L28, l28 = '\u042D', '\u044D'
L29, l29 = '\u042E', '\u044E'
L30, l30 = '\u042F', '\u044F'
maj = (L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18, L19, L20, L21, L22, L23, L24, L25, L26, L27, L28, L29, L30)
minu = (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30)

print("=" * 40)
print("Alphabet cyrillique Russe")
print("=" * 40)
print("\nMajuscules")
print("-" * 40)
for L in range(len(maj)):
    print(L, ':', maj[L])
print("\nMinuscules")
print("-" * 40)
for l in range(len(minu)):
    print(l, ':', minu[l])

alphabetFile = open('alpha.tex', 'w')
alphabetFile.write('\\documentclass[12pt,a4paper]{article}\n')
alphabetFile.write('\\usepackage{fontspec}\n')
alphabetFile.write('\\usepackage{xunicode}\n')
alphabetFile.write(r'\newfontfamily\cyrillicfont{Times New Roman}')
alphabetFile.write('\n\\usepackage{polyglossia}\n')
alphabetFile.write('\\usepackage{xltxtra}\n')
alphabetFile.write('\\setmainlanguage{french}\n')
alphabetFile.write('\\setotherlanguages{russian}\n')
alphabetFile.write('\n\\begin{document}\n')
alphabetFile.write('\\title{Alphabet cyrillique Russe avec Python 3 et \\XeLaTeX}\n')
alphabetFile.write('\\author{Laurent Garnier}\n')
alphabetFile.write('\n\\maketitle\n')
alphabetFile.write('\\section{Majuscules}\n')
alphabetFile.write(r'\begin{center}')
alphabetFile.write('\n \\begin{tabular}{c|c|c}\n')
alphabetFile.write(r'    Indice & Lettre Majuscule & lettre minuscule \\')
alphabetFile.write('\n')
alphabetFile.write(r'    \hline')
alphabetFile.write('\n')
for L in range(len(maj)):
    alphabetFile.write('    ')
    alphabetFile.write(str(L))
    alphabetFile.write(' & ')
    alphabetFile.write(r'\textrussian{')
    alphabetFile.write(maj[L])
    alphabetFile.write('} & ')
    alphabetFile.write(r'\textrussian{')
    alphabetFile.write(minu[L])
    alphabetFile.write('}')
    alphabetFile.write(r' \\')
    alphabetFile.write('\n')
alphabetFile.write('  \\end{tabular}\n')
alphabetFile.write(r'\end{center}')
alphabetFile.write('\n')
alphabetFile.write(r'\section{Quelques exemples}')
alphabetFile.write('\n')
alphabetFile.write(r'\textrussian{а ты говоришь по русски?} = Parles-tu Russe ?')
alphabetFile.write('\n\\end{document}')
alphabetFile.close()
alphabetFile = open('alpha.tex')
content = alphabetFile.read()
alphabetFile.close()
print(content)
