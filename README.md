# PlotNeuralNet
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2526396.svg)](https://doi.org/10.5281/zenodo.2526396)

Latex code for drawing neural networks for reports and presentation. Have a look into examples to see how they are made. Additionally, lets consolidate any improvements that you make and fix any bugs to help more people with this code.

## TODO

- [X] Python interface
- [ ] Add easy legend functionality
- [ ] Add more layer shapes like TruncatedPyramid, 2DSheet etc
- [ ] Add examples for RNN and likes.

## Latex Usage
    see examples
   
## Installation
    
    git clone https://github.com/DavidWatkins/plot_neural_net.git
    cd plot_neural_net
    pip3 install -e . --user
    
## PyUsage

    mkdir my_project
    cd my_project
    vim my_arch.py

        import plot_neural_net
        
        # defined your arch
        arch = [
            plot_neural_net.to_head(),
            plot_neural_net.to_cor(),
            plot_neural_net.to_begin(),
            plot_neural_net.to_conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2),
            plot_neural_net.to_pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
            plot_neural_net.to_conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2),
            plot_neural_net.to_connection("pool1", "conv2"),
            plot_neural_net.to_pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
            plot_neural_net.to_softmax("soft1", 10, "(3,0,0)", "(pool1-east)", caption="SOFT"),
            plot_neural_net.to_connection("pool2", "soft1"),
            plot_neural_net.to_end()
            ]
        
        
        def main():
            name = 'test_simple'
            plot_neural_net.generate_pdf(arch, name)
        
        
        if __name__ == '__main__':
            main()


    python3 my_arch.py
    evince test_simple.pdf

## Examples

Following are some network representations:

<p align="center"><img  src="https://user-images.githubusercontent.com/17570785/50308846-c2231880-049c-11e9-8763-3daa1024de78.png" width="85%" height="85%"></p>
<h6 align="center">FCN-8</h6>


<p align="center"><img  src="https://user-images.githubusercontent.com/17570785/50308873-e2eb6e00-049c-11e9-9587-9da6bdec011b.png" width="85%" height="85%"></p>
<h6 align="center">FCN-32</h6>


<p align="center"><img  src="https://user-images.githubusercontent.com/17570785/50308911-03b3c380-049d-11e9-92d9-ce15669017ad.png" width="85%" height="85%"></p>
<h6 align="center">Holistically-Nested Edge Detection</h6>




