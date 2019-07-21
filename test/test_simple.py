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
