import os
import plot_neural_net.layers
import pdflatex

layers_path = os.path.dirname(os.path.abspath(plot_neural_net.layers.__file__))


def to_head():
    return r"""
\documentclass[border=8pt, multi, tikz]{standalone} 
\usepackage{import}
\import{""" + layers_path + r"""/}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image 
"""


def to_cor():
    return r"""
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}   
"""


def to_begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""


# layers definition

def to_input(image_path, to='(-3,0,0)', width=8, height=8, name="temp"):
    return r"""
\node[canvas is zy plane at x=0] (""" + name + """) at """ + to + """ {\includegraphics[width=""" + str(
        width) + "cm" + """,height=""" + str(height) + "cm" + """]{""" + image_path + """}};
"""


# Conv
def to_conv(name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" "):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name=""" + name + """,
        caption=""" + caption + r""",
        xlabel={{""" + str(n_filer) + """, }},
        zlabel=""" + str(s_filer) + """,
        fill=\ConvColor,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""


# Conv,Conv,relu
# Bottleneck
def to_conv_conv_relu(name, s_filer=256, n_filer=(64, 64), offset="(0,0,0)", to="(0,0,0)", width=(2, 2), height=40,
                      depth=40, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {RightBandedBox={
        name=""" + name + """,
        caption=""" + caption + """,
        xlabel={{ """ + str(n_filer[0]) + """, """ + str(n_filer[1]) + """ }},
        zlabel=""" + str(s_filer) + """,
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height=""" + str(height) + """,
        width={ """ + str(width[0]) + """ , """ + str(width[1]) + """ },
        depth=""" + str(depth) + """
        }
    };
"""


# Pool
def to_pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {Box={
        name=""" + name + """,
        caption=""" + caption + r""",
        fill=\PoolColor,
        opacity=""" + str(opacity) + """,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""


# unpool4,
def to_unpool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {Box={
        name=""" + name + r""",
        caption=""" + caption + r""",
        fill=\UnpoolColor,
        opacity=""" + str(opacity) + """,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""


def to_convres(name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2,
               caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {RightBandedBox={
        name=""" + name + """,
        caption=""" + caption + """,
        xlabel={{ """ + str(n_filer) + """, }},
        zlabel=""" + str(s_filer) + r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity=""" + str(opacity) + """,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""


# ConvSoftMax
def to_conv_softmax(name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" "):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name=""" + name + """,
        caption=""" + caption + """,
        zlabel=""" + str(s_filer) + """,
        fill=\SoftmaxColor,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""


# SoftMax
def to_softmax(name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8,
               caption=" "):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name=""" + name + """,
        caption=""" + caption + """,
        xlabel={{" ","dummy"}},
        zlabel=""" + str(s_filer) + """,
        fill=\SoftmaxColor,
        opacity=""" + str(opacity) + """,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""


def to_connection(of, to):
    return r"""
\draw [connection]  (""" + of + """-east)    -- node {\midarrow} (""" + to + """-west);
"""


def to_skip(of, to, pos=1.25):
    return r"""
\path (""" + of + """-southeast) -- (""" + of + """-northeast) coordinate[pos=""" + str(pos) + """] (""" + of + """-top) ;
\path (""" + to + """-south)  -- (""" + to + """-north)  coordinate[pos=""" + str(pos) + """] (""" + to + """-top) ;
\draw [copyconnection]  (""" + of + """-northeast)  
-- node {\copymidarrow}(""" + of + """-top)
-- node {\copymidarrow}(""" + to + """-top)
-- node {\copymidarrow} (""" + to + """-north);
"""


def to_end():
    return r"""
\end{tikzpicture}
\end{document}
"""


def generate_pdf(arch, pathname="file"):
    outstring = ''.join(arch)
    binary_outstring = outstring.encode('ascii')
    pdfl = pdflatex.PDFLaTeX.from_binarystring(binary_outstring, pathname)
    pdfl.create_pdf(keep_pdf_file=True)
